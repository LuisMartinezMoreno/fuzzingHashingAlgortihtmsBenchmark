import ssdeep
from . import emailComparator

# Function to calculate the ssdeep similarity between two strings
def calculate_similitude_ssdeep(txt1, txt2):
    """
    Calculates the ssdeep similarity between two strings.

    Args:
        txt1 (str): The first string.
        txt2 (str): The second string.

    Returns:
        int: The ssdeep similarity score (the closer to 100, the better).
    """
    hash1 = ssdeep.hash(txt1)
    hash2 = ssdeep.hash(txt2)

    comparison = ssdeep.compare(hash1, hash2)
    return comparison

# Main function to execute ssdeep similarity comparison
def execute(txt1, txt2, archive):
    """
    Executes the ssdeep similarity comparison between two texts and prints the result.

    Args:
        txt1 (str): The first text.
        txt2 (str): The second text.
        archive (str): The path to the archive.

    Returns:
        None
    """
    similitude = calculate_similitude_ssdeep(txt1, txt2)
    print("====== SSDEEP Similitude result for the comparison (the closer the 100 the better)======")
    print(similitude)
    if similitude < 100:
        print("There are some differences, we are working on it ")
        print(emailComparator.main(archive))
    else:
        print("No problems detected\n")
