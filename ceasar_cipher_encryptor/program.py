import string


def caesarCipherEncryptor(s, key):
    alphabet = list(string.ascii_lowercase)
    key = key % 26
    result = ''
    for c in s:
        i = alphabet.index(c)
        i = i + key
        result += alphabet[i]
    return result
