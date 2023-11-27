import tlsh
from . import emailComparator

# Function to calculate the TLSH similarity between two strings
def comparison_similitude_TSLH(txt1, txt2):
    """
    Calculates the TLSH similarity between two strings.

    Args:
        txt1 (str): The first string.
        txt2 (str): The second string.

    Returns:
        int: The TLSH similarity score (the closer to 0, the more similar).
    """
    hash1 = tlsh.hash(txt1.encode('utf-8'))
    hash2 = tlsh.hash(txt2.encode('utf-8'))
    score = tlsh.diff(hash1, hash2)
    return score

# Main function to execute TLSH similarity comparison
def execute(txt1, txt2, archive):
    """
    Executes the TLSH similarity comparison between two texts and prints the result.

    Args:
        txt1 (str): The first text.
        txt2 (str): The second text.
        archive (str): The path to the archive.

    Returns:
        None
    """
    print("====== TLSH Similitude result for the comparison (the closer the 0 the more similar)======")
    similitude = comparison_similitude_TSLH(txt1, txt2)
    print(similitude)
    if similitude > 0:
        print("We have detected some differences, we are working on it ")
        print(emailComparator.main(archive))
    else:
        print("No problems detected\n")
