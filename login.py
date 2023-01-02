users = {'Nathan':'2313','Geez':'pass231','Abebe':'092313133','Miki':"pl3s34D0n'tH4ckM3"}
error=0
while True:

    if error < 5:
        username=input("enter ur name: ")
        password=input("enter ur password: ")
        if username in users and password == users[username]:
            print("welcome to gtst company")
            break
        else :
            print("incorect password or username")
            error+=1
            
    else:
        print("sorry u reached ur maximum trial")
        break


