text=' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def ceaser_bruteforce(cipher_text):
    

    for key in range(len(text)):
        plain_text=''

        for l in cipher_text:
            index=text.find(l)
            index=(index-key)%len(text)
            plain_text=plain_text+text[index]
        print('with key %s,the result is:%s'%(key,plain_text))
        
if __name__=="__main__":
    ceaser_bruteforce('WKLVCLVCDQCH DPSOH')