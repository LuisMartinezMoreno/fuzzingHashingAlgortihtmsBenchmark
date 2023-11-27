import email
from email import policy
from email.parser import BytesParser

# Function to convert .eml file to text
def eml_to_txt(eml_filename):
    """
    Converts the content of a .eml file to text.

    Args:
        eml_filename (str): The path to the .eml file.

    Returns:
        str: The text content extracted from the email.
    """
    with open(eml_filename, 'rb') as eml_file:
        # Parse the .eml file
        msg = BytesParser(policy=policy.default).parse(eml_file)
        # Extract text content from the email
        text_content = ""
        for part in msg.iter_parts():
            if part.get_content_type() == 'text/plain':
                text_content += part.get_payload()
        if text_content == "":
            # If no text/plain part found, fallback to reading the entire file
            return read_file(eml_filename)
        from_email = msg.get("From")
        if from_email != "":
            # Append the "From" email address to the text content
            text_content += from_email
        return text_content

# Function to read the entire content of a file
def read_file(file):
    """
    Reads the entire content of a file.

    Args:
        file (str): The path to the file.

    Returns:
        str: The content of the file.
    """
    with open(file, 'r') as archive:
        content = archive.read()
    return content
