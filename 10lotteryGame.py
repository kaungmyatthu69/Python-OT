import secrets
secureNumber=secrets.SystemRandom()
while True:
    print('___Welcome to Our Game____')
    press1=int(input("press 1 to read rule or Press 2 to Play Game >"))
    if press1==1:
        print('>age must be more than 18')
        print(">Show money more than 5000")
        print('>U must use more than 1000 each time')
    if press1==2:
        uName=input('Please enter your  name :>')
        uAge=int(input('Please enter your age :>'))

        while len(uName)>2 and uAge>=18:
            print('u can play game now')
            print('Welcome :>',uName)
            while True:
                sMoney=int(input("Please enter your show money ;>"))
                while sMoney>=5000:
                    while True:
                        print('This is your money :>',sMoney)
                        inputMoney=int(input('Please enter money to play ;>'))
                        luckyNumber=int(input('Please enter your lucky number :>'))
                        sysemNumber=secureNumber.randint(10,99)
                        while luckyNumber==20:
                            print('You are win in 2D game ')
                            sMoney=sMoney*10
                            print("This is your all money is $",sMoney)
                            toquit=int(input('press 0 to quit form this game >'))
                            if toquit==0:
                                break

                        print('Try again....lucky number is',sysemNumber)
                        sMoney-=inputMoney
                        if sMoney<1000:
                            print('you have not enough money >',sMoney)
                            break
                print('Please more money')
            
        print('Please again read the rule')

      