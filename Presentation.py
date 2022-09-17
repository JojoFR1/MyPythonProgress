#Get user last name
def lastName():
    lastName.user = input("What is your last name?")
    #Ask the user if the last name is correct
    answer = input("Your last name is " + lastName.user + "? - y/n")
    if(answer=="n"):
        lastName() #Go back where the function is defined
lastName() #Run function

#Get user first name
def firstName():
    firstName.user = input("What is your first name?")
    #Ask the user if the first name is correct
    answer = input("Your first name is " + firstName.user + "? -y/n")
    if(answer=="n"):
        firstName() #Go back where the function is defined
firstName() #Run function

#Get user age
def age():
    age.user = input("What is your age?")
    #Ask the user if the age is correct
    answer = input("You're " + age.user + " year old? - y/n")
    if(answer=="n"):
        age() #Go back where the function is defined
age() #Run function

#Get user class
def classe():
    classe.user = input("What is your class?")
    #Ask the user if the class is correct
    answer = input("Your class is " + classe.user + "? - y/n")
    if(answer=="n"):
        classe() #Go back where the function is defined
classe() #Run function

#User information summary
print("Hi, you are " + lastName.user + " " + firstName.user + ", you're " + age.user + " year old and your class is " + classe.user + ".")