#caeser_cipher_+jmj:
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caeser():
   
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = (int(input("Type the shift number:\n")))%26  #whoa this was a great idea.

  li=[]
 

  for i in range(0,(26-shift)):
        li.append(alphabet[i+shift])
  
  for j in range(0,shift):
        li.append(alphabet[j])
  print(li)

#encode:
  new=[]
  if direction=="encode":
        for word in text:
            if word in alphabet:
              new.append(li[alphabet.index(word)])
            else:
              new.append(word)    

#decode:
  elif direction=="decode":
        for word in text:
            if word in alphabet:
               new.append(alphabet[li.index(word)])   
            else:
               new.append(word)     
  for i in range (0,len(text)):
        print(new[i],end="") 
  print() 

  res=input("Do you want to try this out again(y/n)?").lower()  
  if res=="y":
     caeser()
  elif res!='y' and res!='n':
     print("Invalid input!")  

        
caeser()



    
    


