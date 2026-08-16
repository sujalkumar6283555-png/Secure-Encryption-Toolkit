def encrypt(text, key):
    result = ""

    for char in text:
        result += chr(ord(char) ^ key)

    return result


def decrypt(text, key):
    result = ""

    for char in text:
        result += chr(ord(char) ^ key)

    return result
