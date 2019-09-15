text=' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key=3

def caesar_encrypt(plain_text):
        cipher_text=''
        plain_text=plain_text.upper()

        for l in plain_text:
            index=text.find(l)
            index=(index+key)%len(text)
            cipher_text=cipher_text+text[index]
        return cipher_text

def caesar_decrypt(cipher_text):
    plain_text=''

    for l in cipher_text:
        index=text.find(l)
        index=(index-key)%len(text)
        plain_text=plain_text+text[index]
    return plain_text

        
if __name__=="__main__":
    encrypt=caesar_encrypt('This is an example')
    print(encrypt)

    decrypt=caesar_decrypt(encrypt)
    print(decrypt)