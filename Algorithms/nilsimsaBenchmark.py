import nilsimsa
from commons import emailComparator, normalizeData

# Function to calculate the Nilsimsa similarity between two strings
def calculate_similitude_nilsimsa(str1, str2):
    """
    Calculates the Nilsimsa similarity between two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        float: The Nilsimsa similarity score (the closer to 128, the better).
    """
    # Calculate Nilsimsa hashes for both strings
    hash_str1 = nilsimsa.Nilsimsa(str1)
    hash_str2 = nilsimsa.Nilsimsa(str2)

    # Calculate the Hamming distance between the hashes
    distance_hamming = nilsimsa.compare_digests(hash_str1.hexdigest(), hash_str2.hexdigest(), True, True, -100)
    return normalizeData.normalize(distance_hamming,-128,128)

# Main function to execute Nilsimsa similarity comparison
def execute(txt1, txt2, archive):
    """
    Executes the Nilsimsa similarity comparison between two texts and prints the result.

    Args:
        txt1 (str): The first text.
        txt2 (str): The second text.
        archive (str): The path to the archive.

    Returns:
        None
    """
    similitude = calculate_similitude_nilsimsa(txt1, txt2)
    print("====== Nilsima Similitude result for the comparison (the closer the 128 the better)======")
    print(similitude)
    if similitude < 95:
        print("There are some differences, we are working on it ")
        result = emailComparator.main(archive)
        print(result)
    else:
        print("No problems detected\n")
