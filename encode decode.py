#!/usr/bin/env python
# coding: utf-8

# In[2]:


alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m",
         "n","o","p","q","r","s","t","u","v","w","x","y","z"]
if_over=False
while if_over==False:
    try:
        direction=input("type 'encode' to encrypt,type 'decode' to decrypt:\n").lower()
        shift=int(input("type the shift number:\n"))
        text=input("type your msg without space:\n").lower()
    except Exception as e:
        print(e)
        break
    def encode(text,shift):
        encoded=[]
        for i in text:
            start=alphabet.index(i)
            shift_1=start+shift
            if shift_1>=26:
                new=alphabet[(shift_1-26)]
            else:
                new=alphabet[shift_1]
            encoded.append(new)
        print("".join(encoded))



    def decode(text,shift):

        decoded=[]
        for i in text:
            start=alphabet.index(i)
            shift_1=start-shift

            if shift_1<0:
                new=alphabet[(26+shift_1)]
            else:
                new=alphabet[shift_1]
            decoded.append(new)
        print("".join(decoded))

    if direction =="encode":
        alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m",
             "n","o","p","q","r","s","t","u","v","w","x","y","z"]
        encode(text,shift)
    elif direction =="decode":
        alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m",
             "n","o","p","q","r","s","t","u","v","w","x","y","z"]
        decode(text,shift)
    ask=input("do u want to code again 'yes' or 'no': ").lower()

    if ask=="yes":
        if_over=False
    elif ask=="no":
        if_over=True

    

    


# In[ ]:




