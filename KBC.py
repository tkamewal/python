import sys
ammount=0
ques1=["What is the capital of india: ","a. Mumbai","b. Chhenai","c. jaipur","d. Delhi"]
ques2=["Who is the national bird of india: ","a. Peakock","b. Parrot","c. Spparow","d. Peigon"]
ques3=["Who is the national animal of india: ","a. Lion","b. dog","c. Tiger","d. cat"]
print(ques1[0])
print(ques1[1])             
print(ques1[2])               
print(ques1[3])               
print(ques1[4])               
x=input("Enter your answer: ")
if(x=="d"):
    print("correct answer!!")
    ammount=2000
    print("You have won 2000 ruppes")
else:
    print("Wrong answer ! you have lost")
    print("take back home money: ",ammount) 
    sys.exit()   
print(ques2[0])
print(ques2[1])             
print(ques2[2])               
print(ques2[3])               
print(ques2[4])               
y=input("Enter your answer: ")
if(y=="a"):
    print("correct answer!!")
    ammount=4000
    print("You have won 4000 ruppes")
else:
    print("Wrong answer ! you have lost")
    print("take back home money: ",ammount)
    sys.exit()
print(ques3[0])
print(ques3[1])             
print(ques3[2])               
print(ques3[3])               
print(ques3[4])               
z=input("Enter your answer: ")
if(z=="c"):
    print("correct answer!!")
    ammount=10000
    print("You have won 10000 ruppes")
else:
    print("Wrong answer ! you have lost")
    print("take back home money: ",ammount)
    sys.exit()