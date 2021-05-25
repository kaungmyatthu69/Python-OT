#calcultor program
print("Press 1 ; for add ")
print ("Press 2; for subsract")
print("Press 3 ; for multiplty")
print("Press 4 ;for divide ")
userInput=input("Please enter somehing >")
firstNumber=int(input("Please enter first number >"))
secondNumber=int(input("Please enter second nuber >"))
if userInput=="1":
    result =firstNumber+secondNumber
elif userInput=='2':
    result=firstNumber-secondNumber
elif userInput=='3':
    result=firstNumber*secondNumber
elif userInput=='4':

    result=firstNumber/secondNumber
else:
    print("You must be enter 1/2/3/4")
print("you result of {} and {} is {}".format(firstNumber,secondNumber,result))
