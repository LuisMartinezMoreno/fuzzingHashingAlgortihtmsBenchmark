import ssdeep
from . import emailComparator


def calculate_similitude_ssdeep(txt1, txt2):
    hash1 = ssdeep.hash(txt1)
    hash2 = ssdeep.hash(txt2)

    comparison = ssdeep.compare(hash1, hash2)
    return comparison

def execute(txt1,txt2, archive):
    similitude = calculate_similitude_ssdeep(txt1, txt2)
    print("====== SSDEEP Similitude result for the comparison (the closer the 100 the better)======")
    print(similitude)
    if(similitude<100):
        print("There are some differences, we are working on it ")
        print(emailComparator.main(archive))
    else:
        print("No problems detected\n")

