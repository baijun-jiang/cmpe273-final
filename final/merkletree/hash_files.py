import hashlib
from pathlib import Path

def read_files_and_hash(path):
    hash_dict = {}
    for filepath in Path(path).glob('**/*'):
        print(filepath)
        try:
            file_reader = open(filepath)
            hash_data = hashlib.sha256(file_reader.read().encode())
            print(hash_data.hexdigest())
            hash_dict[hash_data.hexdigest()] = str(filepath)
        finally:
            file_reader.close()
    
    return hash_dict



