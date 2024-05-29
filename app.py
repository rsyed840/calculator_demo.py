from cal_func import addition,substraction   

def main():
    print("welcome to the Calculator App")
    print("""
          select the function from given options 
          1.Add
          2.Substract
          """)
    
    user_input=input("select function")
    a=int(input("value of A "))
    b=int(input("value of B "))
    
    if user_input=="1":
        result=addition(a,b)
    elif user_input=="2":
        result=substraction(a,b)
    
    print("Result:", result)
    
if __name__=="__main__":
        main()
        