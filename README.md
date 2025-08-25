1. Caesar cipher is a simple substitution cipher.
2. Here every letter of the alphabet is mapped to another letter of the alphabet.
3. Mathematically it can be represented as : y=(x+key)mod26.
4. Every letter in the alphabet is assigned a number, a is assigned 0, b is assigned 1 and similarly for the rest of the alphabets till z which is assigned 25.
5. The key belongs to the set {0,1,2,......,25}.
6. The 'shift' is calculated by the above mathematical function and for the decrytion of a cipher text the mathematical representation is : x=(y-key)mod26.
7. In the code for encryption and decryption some loopholes are not taken care of. However, in the second peice of code those loopholes have been taken care of.

Note: This code is just for educational purpose, it is not built for real world applications.
This is one of the first codes I have written during my study of cryptology.
