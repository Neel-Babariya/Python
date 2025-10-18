print("Login Page")

age = int(input("enter your age here")) 

if age >= 18 :
  pass
else :
  print("you must be 18") 

name = input("enter your name here: ") 
letters = name.count() 

if letters == 0 :
  print(" please enter a valid username: ") 
elif letters <= 12 :
  print (" you are signed in! ") 
else :
  print(" the username must be shorter than 12 characters") 
