import hashlib
from hashlib import sha256
import csv

hash_set = {}
def calc_hash():
    for i in range(1000,9999):
        m = sha256()
        m.update(str(i).encode("utf-8"))
        hash = m.hexdigest()
        hash_set[hash]=i

def hash_password_hack(input_file_name, output_file_name):
    calc_hash()
    result=[]
    with open(input_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            val = hash_set.get(row[1])
            result.append((row[0],val))
    with open(output_file_name,"w") as f:
        for item in result:
            f.write(str(item[0]+','+str(item[1]))+"\n")
        f.close()



