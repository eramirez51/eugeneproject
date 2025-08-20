import hashlib

def SHA1(msg: str) -> str:
    return hashlib.sha1(msg.encode()).hexdigest()

print(SHA1("Test2"))
