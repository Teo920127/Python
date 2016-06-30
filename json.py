import json

_dict=(json.load(open('e:/a.txt')))
print(type(_dict))
print(type(_dict['errno']))

username=input("username :")
if username in _dict:
    for i in range(5):
        userpasswd = int(input("password: "))
        if userpasswd == _dict[username]:
            print("login!")
            print (i)
            break
        else:
            print("error")
else:
    print("没有此用户名")

print("for is over")

