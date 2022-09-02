"""
Created on Tue Jun 14 10:02:51 2022
@author: Gyanesh Raj
"""
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
A=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
class Ceasar():
    def __init__(this,text=str("Plain or Cipher"),key=int(3)):
        this.text=text;
        this.key=key;
    def additive_encryption_process(this):
        ct=str();n=(key//26)+1;
        for i in text:
            if i in a:i=a[a.index(i)+(key)-n*26];ct=ct+i;
            elif i in A:i=A[A.index(i)+(key)-n*26];ct=ct+i;
            else:ct=ct+i;
        return ct;
    def subtractive_encryption_process(this):
        ct=str();n=(key//26);
        for i in text:
            if i in a:
                t=a.index(i)-(key)+n*26
                if t<0:i=a[t+26];ct=ct+i;
                else:i=a[t];ct=ct+i;
            elif i in A:
                T=A.index(i)-key+n*26
                if T<0:i=A[T+26];ct=ct+i;
                else:i=A[T];ct=ct+i;
            else:ct=ct+i;
        return ct;
    def additive_encryption(this):
        print("The Cipher text is :",Ceasar.additive_encryption_process(this));
    def additive_decryption(this):
        print("The plain text is :",Ceasar.subtractive_encryption_process(this));
    def subtractive_encryption(this):
        print("The Cipher text is :",Ceasar.subtractive_encryption_process(this));        
    def subtractive_decryption(this):
        print("The plain text is :",Ceasar.additive_encryption_process(this));
###---------------------------------------------------------------###



###---------------------------------------------------------------###
import msvcrt;
text=str(input("Enter the text: "));key=int(input("Enter the key: "));
print("Options:");print("1-Additive Encryption");print("2-Subtractive Encryption");print("3-Additive Decryption");print("4-Subtractive Decryption");
opt=int(input("Select the option:" ));
g=Ceasar(text,key);
if opt==1:Ceasar.additive_encryption(g);
elif opt==2:Ceasar.subtractive_encryption(g);
elif opt==3:Ceasar.additive_decryption(g);
elif opt==4:Ceasar.subtractive_decryption(g);
msvcrt.getch();