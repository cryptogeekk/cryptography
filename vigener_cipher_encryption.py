alphabet=' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere_encryption(plain_text,key):
    plain_text=plain_text.upper()
    key=key.upper()
    
    key_index=0
    cipher_text=''

    for characters in plain_text:
        index=(alphabet.find(characters)+alphabet.find(key[key_index]))%len(alphabet)
        cipher_text=cipher_text+alphabet[index]
        key_index=key_index+1

        if key_index==len(key):
            key_index=0

    return cipher_text 

def vigenere_decryption(cipher_text,key):
    cipher_text=cipher_text.upper()
    key=key.upper()

    key_index=0
    plain_text=''

    for characters in cipher_text:
         index=(alphabet.find(characters)-alphabet.find(key[key_index]))%len(alphabet)
         plain_text=plain_text+alphabet[index]
         key_index=key_index+1

         if key_index==len(key):
             key_index=0
    
    return plain_text

if __name__ == "__main__":
    text='Hey this ia an example of vigenere encryption'
    key1='secret'
    encrypted=vigenere_encryption(text,key1)
    print('Encrypted message is : %s' % encrypted)
    decrypted=vigenere_decryption(encrypted,key1)
    print('\nDecrypted message is: %s' % decrypted)






        
     
       
    
                
