import email
from email import policy
from email.parser import BytesParser

def eml_to_txt(eml_filename):
    with open(eml_filename, 'rb') as eml_file:
        # Parse the .eml file
        msg = BytesParser(policy=policy.default).parse(eml_file)
        # Extract text content from the email
        text_content = ""
        for part in msg.iter_parts():
            if part.get_content_type() == 'text/plain':
                text_content += part.get_payload()
        if(text_content == ""):
            return read_file(eml_filename)
        from_email = msg.get("From")
        if(from_email!=""):
            text_content+=from_email
        return text_content

def read_file(file):
    with open(file, 'r') as archive:
        content = archive.read()
    return content       