import hashlib

# Hash user's password 
def make_pw_hash(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


# verify entered password against previously hashed password in db
def check_pw_hash(password, hash):
    if make_pw_hash(password) == hash:
        return True

    return False