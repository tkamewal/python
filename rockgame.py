import random
while True:
 user=input("Enter your choice(Stone, Paper, Scissors):")
 comp_choice=["stone","paper","scissor"]
 comp=random.choice(comp_choice)
 print(f"Your choice:  {user} and computer choice:  {comp}")
    
 if(user==comp):
  print(f"It's a tie Both choose same:{user}")
 elif(user=="stone"):
    if(comp=="scissor"):
        print("You won the game!! ,as rock smashes scissor")
    else:
        print("You loss as paper folds rock!!")    
 elif(user=="paper"):
   if(comp=="stone"):
        print("You won the game!! ,as paper folds rock")
   else:
        print("You loss as Scissor cuts paper!!")     
 elif(user=="scissor"):
    if(comp=="paper"):
        print("You won the game!! ,as scissor cuts paper")
    else:
        print("You loss as rock takes scissor down!!")  
 try_again=input("Try Again?(y/n) :")  
 if(try_again.lower()!="y"):
  break  
       

