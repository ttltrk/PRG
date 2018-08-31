
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [C](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [scripts](https://github.com/ttltrk/PRG/blob/master/APPS.MD)

---

### DreamCars 1.0

---

```python

'''
*********************************************************************
*
* Login part
*
*********************************************************************
'''

user_pwd = int(input('add your pwd in numerical format... \n'))
user_name = input('setup your name... \n')
user_role = int(input('1. - press [1] if you want BUY a car \n2. - press [2] if you want SELL a car... \n'))
user_crd = int(input('1. - if you a seller press [0] \n2. - if you want BUY a car then add your credit frame in [EUR] \n'))
login_q = int(input('please type your pwd once again... \n'))

def wrongpwd():
    print('wrong pwd')

def pwdCheck():
    if login_q != user_pwd:
        return wrongpwd()
    else:
        print(' ')
        print('Welcome on the DreamCars 1.0')
        print(' ')
        return again()

'''
*********************************************************************
*
* inside the app
*
*********************************************************************
'''

def again():
    return mainConsole()

def exit():
    print('bye')

'''
*********************************************************************
*
* Home section
*
*********************************************************************
'''

def checkHome():
    welcome = 'Welcome on the DreamCars 1.0, the place where you can buy or sell, car(s)'
    print(' ')
    print('---------------------------------------------------------------------------------')
    print(welcome)
    print('---------------------------------------------------------------------------------')
    print(' ')
    return again()

'''
*********************************************************************
*
* Profile end
*
*********************************************************************
'''

def checkProfileBuyer():
    b_role = 'buyer'
    ld = ['name:', 'role:', 'pwd:', 'crd in EUR:']
    ll = [user_name, b_role, user_pwd, user_crd]
    zipl = zip(ld, ll)
    dictl = dict(zipl)
    for key in dictl:
        print(key, dictl[key])
    return again()

def checkProfileSeller():
    s_role = 'seller'
    ld = ['name:', 'role:', 'pwd:']
    ll = [user_name, s_role, user_pwd]
    zipl = zip(ld, ll)
    dictl = dict(zipl)
    for key in dictl:
        print(key, dictl[key])
    return again()

def checkProfileSUser():
    su_role = 'Super User / Admin'
    print(su_role)
    return again()

def checkProfile():
    cpr = ' '
    if user_role == 1:
        cpr = checkProfileBuyer()
    elif user_role == 2:
        cpr = checkProfileSeller()
    else:
        cpr = checkProfileSUser()
    return cpr

'''
*********************************************************************
*
* Profile start
*
* Adv end
*
*********************************************************************
'''

mainListOfCars1 = []
mainListOfCars2 = []
mainListOfCars3 = []
mainListOfCars4 = []

def listOfCars():
    print(mainListOfCars1)
    print(mainListOfCars2)
    print(mainListOfCars3)
    print(mainListOfCars4)
    return again()

def checkAdvAsBuyer():
    buyAcar = 'which car do you need, check out the List of cars topic'
    print(buyAcar)
    return again()

def checkAdvAsSeller():
    print('add the parameters')
    carType = input('type = ')
    carYear = int(input('year =')) # 2018-2015 = 10, 2014-2010 = 8, 2009-2005 = 6, 2004 - = 4
    carHP = int(input('hp = ')) # -100 = 4, 101-200 = 6, 201 - 450 = 8, 451 - = 10
    carlk = int(input('l/km =')) # -5 = 10, 6-10 = 8, 11-15 = 6, 16- = 4
    carVal1 = ' '
    carVal2 = ' '
    carVal3 = ' '
    if carYear > 2014:
        carVal1 = 10
    elif carYear < 2014:
        carVal1 = 8

    if carHP > 100:
        carVal2 = 10
    elif carHP < 100:
        carVal2 = 8

    if carlk < 10:
        carVal3 = 10
    elif carlk > 10:
        carVal3 = 8

    carVal = carVal1 + carVal2 + carVal3
    if carVal > 25:
        carPrice = 20000
    elif carVal <20 and carVal > 15:
        carPrice = 10000
    else:
        carPrice = 5000

    paramList = [carType, carYear, carHP, carlk, carVal, carPrice]
    if mainListOfCars1 == []:
        mainListOfCars1.append(paramList)
    elif mainListOfCars2 == []:
        mainListOfCars2.append(paramList)
    elif mainListOfCars3 == []:
        mainListOfCars3.append(paramList)
    else:
        mainListOfCars4.append(paramList)
    return listOfCars()

def checkAdvAsAdmin():
    advasadm = ('modify or delete')
    print(advasadm)
    return again()

def checkAdvertisement():
    catr = ' '
    if user_role == 1:
        catr = checkAdvAsBuyer()
    elif user_role == 2:
        catr = checkAdvAsSeller()
    else:
        catr = checkAdvAsAdmin()
    return catr

'''
*********************************************************************
*
* Adv start
*
* Adm end 
*
*********************************************************************
'''

def checkAdmBuyer():
    b_admin1 = '1 - Accept'
    print(b_admin1)
    return again()

def checkAdmSeller():
    s_admin1 = '1 - Advertisement'
    s_admin2 = '2 - Modify'
    s_admin3 = '3 - Remove'
    s_admin4 = '4 - back to the menu'
    casr = ' '
    ls = [s_admin1, s_admin2, s_admin3, s_admin4]
    print(ls)
    chosenAdmSeller = int(input('choose one option - 1, 2, 3, 4'))
    if chosenAdmSeller == '1':
        return checkAdvAsSeller()
    elif chosenAdmSeller == '2':
        return again()
    elif chosenAdmSeller == '3':
        return again()
    else:
        return again()

def checkAdmSUser():
    su_admin1 = '1 - Remove'
    su_admin2 = '2 - Modify'
    lsu = [su_admin1, su_admin2]
    print(lsu)
    return again()

def checkAdm():
    car = ' '
    if user_role == 1:
        car = checkAdmBuyer()
    elif user_role == 2:
        car = checkAdmSeller()
    else:
        car = checkAdmSUser()
    return car

'''
*********************************************************************
*
* Adm start
* Main Console
*
*********************************************************************
'''

def mainConsole():
    while True:
        a = input('---------------------------------------------------------------------------------------------------- \n |  '
                  'H = Home  |  P = Profile  |  '
                  'M = Adm  |  A = Advertisement  |  L = List of Cars  |'
                  '  X = Exit |\n---------------------------------------------------------------------------------------------------- \n \n ')
        mcr = ' '
        if a == 'h':
            mcr = checkHome()
        elif a == 'p':
            mcr = checkProfile()
        elif a == 'a':
            mcr = checkAdvertisement()
        elif a == 'm':
            mcr = checkAdm()
        elif a == 'l':
            mcr = listOfCars()
        elif a == 'x':
            mcr = exit()
        return mcr

pwdCheck()
#again()```
