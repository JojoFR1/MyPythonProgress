## Programme du 15/09/2022 (thanks to Bebert for help)
## Dernière modification le 24/09/2022

#Get user last name
def getLastName():
    return input("What's your last name? ")

#Get user first name
def getFirstName():
    return input("What's your first name? ")


#Get user age
def getAge():
    #Verify if the age is a positive integer
    ageIsValid = False
    while(not ageIsValid):
        age = input("What's your age? ")
        if age.isdigit():
            age = int(age)
            if age>0:
                ageIsValid = True
    return age

#Get user class
def getClass():
    return input("What's your class? ")

#Get all data
dataIsValid = False

while(not dataIsValid):
    lastName = getLastName()
    firstName = getFirstName()
    age = getAge()
    userClass = getClass()
    if input("Is this correct? Y/N").lower() == "y":
        dataIsValid = True

#User information summary
print(f"Hi, you are {lastName} {firstName}, you're {age} years old and your class is {userClass}.")