import email
from email import policy
from email.parser import BytesParser
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse

# Function to extract the "From" email address from an email file
def extract_from_email(eml_filename):
    """
    Extracts the "From" email address from the given email file.

    Args:
        eml_filename (str): The path to the .eml file.

    Returns:
        str: The "From" email address.
    """
    with open(eml_filename, 'rb') as eml_file:
        # Parse the .eml file
        msg = BytesParser(policy=policy.default).parse(eml_file)

        # Extract the "From" email address
        from_email = msg.get("From")

        return from_email

# Function to extract links from an email file
def extract_links(eml_filename):
    """
    Extracts links from the given email file.

    Args:
        eml_filename (str): The path to the .eml file.

    Returns:
        list: A list of cleaned and filtered links.
    """
    with open(eml_filename, 'rb') as eml_file:
        # Parse the .eml file
        msg = BytesParser(policy=policy.default).parse(eml_file)

        # Initialize a list to store extracted links
        links = []

        # Function to extract links from HTML content
        def extract_links_from_html(html_content):
            soup = BeautifulSoup(html_content, 'html.parser')
            for link in soup.find_all('a', href=True):
                links.append(link.get('href'))

        # Extract links from different parts of the email
        for part in msg.iter_parts():
            content_type = part.get_content_type()

            if content_type == 'text/html':
                # Extract links from HTML content
                extract_links_from_html(part.get_payload(decode=True).decode('utf-8'))
            elif content_type == 'text/plain':
                # Extract links from plain text content using a simple regex
                text_content = part.get_payload(decode=True).decode('utf-8')
                urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text_content)
                links.extend(urls)

        # Clean and filter the extracted links
        cleaned_links = [link for link in links if link is not None]
        return cleaned_links

# Function to check if the sender email is in a whitelist
def checkMailWhiteList(emails):
    """
    Checks if the sender email is in a whitelist.

    Args:
        emails (str): Comma-separated string of email addresses.

    Returns:
        tuple: A boolean indicating whether the sender is in the whitelist, and a list of untrusted sources.
    """
    if emails:
        eachEmail = emails.split(",")
        result = []
        for email in eachEmail:
            tmp = email.split("@")
            result.append(tmp[1][:-1])
        if len(result) > 0:
            for res in result:
                if res != "spotify.com":
                    return False, result
        return True, ""
    return True, None

# Function to check if links are from trusted sources
def checkKnownLinkSource(links):
    """
    Checks if links are from known, trusted sources.

    Args:
        links (list): List of links.

    Returns:
        tuple: A boolean indicating whether links are from trusted sources, and a list of untrusted sources.
    """
    if len(links) > 0:
        sources = []
        for link in links:
            firstSplit = link.split("//")
            secondSplit = firstSplit[1].split("/")
            sources.append(secondSplit[0])
        untrustedSources = string_in_file(sources)
        if len(untrustedSources) > 0:
            return False, untrustedSources
        return True, ""
    return True, None

# Function to check if a string is in a list of trusted sources
def string_in_file(string_to_check):
    """
    Checks if a string is in a list of trusted sources.

    Args:
        string_to_check (list): List of strings.

    Returns:
        list: List of untrusted sources.
    """
    trustedSources = ["support.spotify.com", "www.spotify.com", "itunes.apple.com", "play.google.com"]
    untrusted = []
    for i in string_to_check:
        if i not in trustedSources:
            untrusted.append(i)
    else:
        return untrusted

# Main function to analyze an email file
def main(eml_filename):
    """
    Analyzes the given email file and returns a result message.

    Args:
        eml_filename (str): The path to the .eml file.

    Returns:
        str: Result message indicating the analysis outcome.
    """
    from_email = extract_from_email(eml_filename)
    resultCheckFrom, source = checkMailWhiteList(from_email)
    result = ""
    if resultCheckFrom is False:
        result = "Email from an unknown source: " + ", ".join(source) + "\n"

    links_email = extract_links(eml_filename)
    resultCheckLinks, sourceLink = checkKnownLinkSource(links_email)

    if resultCheckLinks is False:
        result += "Email containing an unknown source: " + ", ".join(sourceLink) + "\n"

    if source is None and sourceLink is None:
        result = "This Email does have the expected format\n"
    return result
