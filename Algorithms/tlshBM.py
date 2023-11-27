import tlsh
from . import emailComparator

def comparison_similitude_TSLH(txt1,txt2):
    hash1 = tlsh.hash(txt1.encode('utf-8'))
    hash2 = tlsh.hash(txt2.encode('utf-8'))
    score = tlsh.diff(hash1,hash2)
    return score

def execute(txt1, txt2, archive):
    print("====== TLSH Similitude result for the comparison (the closer the 0 the more similar)======")
    similitude = comparison_similitude_TSLH(txt1, txt2)
    print(similitude)
    if similitude > 0:
        print("We have detected some differences, we are working on it ")
        print(emailComparator.main(archive))
    else:
        print("No problems detected\n")