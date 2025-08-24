#Construction of Caeser Cipher(Encryption+decryption)

#Encryption function:
def caeser_encryption(plaintext):
    key=input("Enter the key: ")#The input must be an integer and between 0 and 26(0 included)
    try:
       key=int(key)
       ciphertext=''
       for char in plaintext:
        real_ord=ord(char)#The ord() function returns the ASCII value
        real_ord=real_ord-97
        shift=(real_ord+key)%26
        shift=shift+97
        ciphertext=ciphertext+chr(shift)#The chr function gives the character corresponding to the ACSII value

       return ciphertext 
    except:
       print("The key must be an integer")



#x=input("Enter the plaintext: ")
#y=caeser_encryption(x)
#print("The cipher text is:", y)

#Decryption function:
def caeser_decryption(ciphertext):
   key=input("Enter the key: ")
   try:
     key=int(key)
     plaintext=''
     for char in ciphertext:
      shift=ord(char)-97
      real_ord=(shift-key)%26
      real_ord=real_ord+97
      plaintext=plaintext+chr(real_ord)

     return plaintext
   except:
     print("The key must be an integer")


y=input("Enter the ciphertext: ")
x=caeser_decryption(y)
print("The plain text is:",x)


