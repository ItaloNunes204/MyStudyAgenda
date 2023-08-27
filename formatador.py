import hashlib


# aplica a criptografia MD5 na senha.
def codificando(senha):
    result = hashlib.md5(senha.encode())
    return str(result.hexdigest())
