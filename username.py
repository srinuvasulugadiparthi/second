for i in range(3):
    username=input("enter your username:")
    password=input("enter your password:")
    if username=="srinu" and password=="1234":
        print("access perimited")
        break
    else:
        print("access deinied")
        print("try agin")
else:
    print("no more attempts for the day")


