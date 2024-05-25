def func1():
    try:
        l=[1,2,3,4,5]
        i=int(input("enter a index: "))
        print(l[i])
        return 1
    except:
        print("You will give a wrong index....")
        return 0
    finally: 
     print("is still i execute")
x=func1()
print(x)