import nilsimsa
from . import emailComparator

def calculate_similitude_nilsimsa(str1, str2):
    # Calcula los hash de Nilsimsa para ambas cadenas
    hash_str1 = nilsimsa.Nilsimsa(str1)
    hash_str2 = nilsimsa.Nilsimsa(str2)

    # Calcula la distancia de Hamming entre los hashes
    distance_hamming = nilsimsa.compare_digests(hash_str1.hexdigest(), hash_str2.hexdigest(),True,True, -100)

    return distance_hamming


def execute(txt1,txt2, archive):
    similitude = calculate_similitude_nilsimsa(txt1, txt2)
    print("====== Nilsima Similitude result for the comparison (the closer the 128 the better)======")
    print(similitude)
    if(similitude<128):
        print("There are some differences, we are working on it ")
        result = emailComparator.main(archive)
        print(result)
    else:
        print("No problems detected\n")
