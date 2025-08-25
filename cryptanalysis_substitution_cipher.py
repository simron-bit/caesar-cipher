#Cryptanalysis of a substitution cipher(Caeser Cipher) by brute force attack:

ciphertext=input("Enter the ciphertext: ")
for key in range(26):#Brute force attack: Exhaustive key search
    plaintext=''
    for char in ciphertext:
        if char.isalpha():#Only letters are encrypted
          shift=ord(char.lower())-97#Converting every possible uppercase letter to a lowercase letter with char.lower()
          real_ord=(shift-key)%26
          real_ord=real_ord+97
          plaintext=plaintext+chr(real_ord)
        else: 
            plaintext+=char#spaces and special characters are retained
    print(plaintext)
    x=input("If the plaintext makes sense please enter 1 or else enter 0")
    x=int(x)
    if x==1:
        break
    if x==0:
        continue
if x==1:
    print("The plaintext is :",plaintext)
    print("The key is: ",key)


   
   