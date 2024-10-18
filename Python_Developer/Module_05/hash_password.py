import hashlib


def _hash_password(password):
    hash = hashlib.sha256(password.encode()).hexdigest()
    hash_int = int(hash, 16)
    return hash_int


if __name__ == '__main__':
   print(_hash_password('elenamaratovnasineva'))
   print(_hash_password('yuryveniaminovichsinev'))