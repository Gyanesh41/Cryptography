"""
Created on Mon May  2 14:37:54 2022
@author: Gyanesh Raj
"""
class railfence():
    def __init__(self,text=str('Plain or Cipher'),key=int(3)):
        self.text=text;
        self.key=key;
    def encryption(self):
        Plain=self.text;count=len(Plain);key=self.key;
        a=[[("_")for i in range(count)]for j in range(key)];
        railfence.locationmarking(a,count,key);ct=[];
        for i in range(key):
            for j in range (count):
                if a[i][j]!="_":a[i][j]=Plain[j];ct.append(Plain[j]);
            print(a[i])
        Cipher="".join(ct);
        print("Cipher Text:",Cipher)
    def locationmarking(matrix,strlength,key):
        row=0;flag=0;
        for i in range(strlength):
            matrix[row][i]="*";
            if flag==0:row+=1;
            else:row-=1;
            if row==0:flag=0;
            elif row==key-1:flag+=1;
        return matrix;
    def decryption(self):
        Cipher=self.text;key=self.key;count=len(Cipher);
        a=[[("_")for i in range(count)]for j in range(key)];
        railfence.locationmarking(a,count,key);pt=[];index=0;
        for i in range(key):
            for j in range(count):
                if a[i][j]!="_":a[i][j]=Cipher[index];index+=1;
            print(a[i]);
        row=0;flag=0;
        for i in range(count):
            pt.append(a[row][i]);
            if flag==0:row+=1;
            else:row-=1;
            if row==0:flag=0;
            elif row==key-1:flag+=1;
        Plain="".join(pt)
        print("Plain text:",Plain);
# =============================================================================
import msvcrt;
Text=str(input("Enter the string:"));
Key=int(input("Enter the key:"));
opt=int(input("Enter 1-Encryption or 2-Decryption:"))
g=railfence(Text,Key)
if opt==1:
    railfence.encryption(g);
elif opt==2:
    railfence.decryption(g);
else:
    print("!!Wrong Input!! Retry");
msvcrt.getch();