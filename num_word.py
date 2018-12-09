#this program asks for input (integer) between 1 and 9999 and returns
#the number in words
n=int(input('please enter an integer between 1 and 9999: '))
num_word1=["zero","one","two","three","four","five","six","seven","eight","nine"]
num_word2=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
num_word3=["irrelevant",num_word2,"twenty ","thirty ","forty ","fifty ","sixty ","seventy ","eighty ","ninety "]
num_word4=["irrelevant",num_word2,"twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
if n/1000>=1:
    i=int(n/1000)
    n=n-(1000*i)
    if n!=0:
        print(num_word1[i],"thousand ",end= "")
    else :
        print(num_word1[i],"thousand")
if n/100>=1:
    i=int(n/100)
    n=n-100*i
    if n!=0:
        print(num_word1[i],"hundred ",end= "")
    else :
        print(num_word1[i],"hundred")
if n/10>=1:
   i=int(n/10)
   if i==1:
       j=n-10
       print(num_word2[j])
   else:
       n=n-10*i
       if n>0:
           print(num_word3[i],end= "")
           print(num_word1[n])
       elif n==0:
           print(num_word4[i])
else :
    if n!=0:
        print(num_word1[n])
       
