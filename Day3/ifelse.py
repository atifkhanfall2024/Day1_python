

   # if , ifelse , elif 
name_character = input("Enter your name ")

Total_characters = 10 

if len(name_character)<Total_characters:
   print("Your name characters is less than 10 characters Try Again !"  , len(name_character))
elif len(name_character)>Total_characters:
   print("Your name characters is more than 10 characters Try Again !" , len(name_character))
else:
   print(" Yes you got it ! Your name characters is exactly 10 characters" , len(name_character))