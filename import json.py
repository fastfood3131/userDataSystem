import json
from os import remove
try:
    with open("data.json") as f:
        datas = json.load(f)
except:
    datas = {}

data = datas
i = 0


class Datastore:
    def __init__(self, user_name=None, password=None):
        if data.get("name") and data.get("password"):
            self.user_name = data.get("name")
            self.password = data.get("password")
        else:
            self.password = password
            self.user_name = user_name

    def create_account(self):
        global i
        global data
        while True:
            if self.password is None and self.user_name is None:
                print("lets create an account!\n")
                user_name = input("name(over 3 char and under 15 char):\n")
                password = input("\npassword(over 3 char and under 15 char):\n")
                password2 = input("enter your password again:\n")
                if len(user_name) > 15:
                    print("your name cant be over 15 char.\n")
                    continue
                elif len(user_name) < 3:
                    print("your name cant be under 3 char.\n")
                    continue
                elif len(password) < 3:
                    print("your password cant be under 3 char.\n")
                    continue
                elif user_name.count(" ") >= 1:
                    print("your name cant have space in it\n")
                    continue
                elif password.count(" ") >= 1:
                    print("your password cant have space in it\n")
                    continue
                elif password2 != password:
                    print("Your password doesn't match your second password\n")
                elif password2 == password:
                    print("your account has been created!\n")
                    data.update(name=user_name, password=password)
                    with open("data.json", "w+") as dataObject:
                        dataObject.write(json.dumps(data, indent=1))
                    print("press anything to escape")
                    input1 = input()
                    if input1:
                        print("User Escape(going to the inside acts)")
                        break
            else:
                if i == 4:
                    print("You've tried to enter your account too many times!")
                    break
                data.update(name=self.user_name, password=self.password)
                print("you already have an account")
                print("\nplease enter your information")
                name_input = input("username: ")
                pass_input = input("password: ")
                if name_input == self.user_name and pass_input == self.password:
                    with open("data.json", "w+") as dataObject:
                        dataObject.write(json.dumps(data, indent=1))
                    print("Login successful!")
                    print("---------------------------------")
                    print("press any key to escape\n")
                    input1 = input()
                    if input1:
                        print("User Escape(going to the inside acts)")
                        break
                else:
                    print("Login Unsuccessful!")
                    i += 1
                    continue

    def inside_acts(self):
        global i
        global data
        while True:
            print("\n1.Change Password")
            print("2.Change Username")
            print("3.Delete Data(!)")
            print("4.Exit")
            input1 = input()
            if input1 == "4":
                break
            elif input1 == "1":
                password = data.get("password")
                pass_input = input("enter your previous password\n")
                if pass_input == password:
                    new_pass_input = input("\nenter your new password:\n")
                    new_pass_input2 = input("\nenter your new password again:\n")
                    if new_pass_input == new_pass_input2 and len(new_pass_input) >= 3 and len(new_pass_input2) <= 15:
                        data.update(password=new_pass_input)
                        with open("data.json", "w+") as dataObject:
                            dataObject.write(json.dumps(data, indent=1))
                        print("password updated!")
                        print("press any key to escape")
                        input2 = input()
                        if input2:
                            print("Escaped")
                            continue
                    else:
                        print("please enter the same password next time\n"
                              "or the name you entered is under 3 char.\n"
                              "or over 15 char")
                        continue
                else:
                    print("invalid password\n")
                    continue
            elif input1 == "2":
                username = data.get("name")
                name_input = input("enter your previous username\n")
                if name_input == username:
                    new_name_input = input("\nenter your new username:\n")
                    new_name_input2 = input("\nenter your new username again:\n")
                    if new_name_input == new_name_input2:
                        data.update(name=new_name_input)
                        with open("data.json", "w+") as dataObject:
                            dataObject.write(json.dumps(data, indent=1))
                        print("username updated!")
                        print("press any key to escape\n")
                        input2 = input()
                        if input2:
                            print("Escaped")
                    else:
                        print("please enter the same username next time")
                else:
                    print("invalid username\n")
                    continue
            elif input1 == "3":
                print("Are you sure(Y/N)")
                input3 = input()
                if input3.lower() == "n":
                    print("Delete data canceled")
                    continue
                elif input3.lower() == "y":
                    try:
                        remove("data.json")
                        print("Data successfully removed")
                        break
                    except FileNotFoundError:
                        print("Data file not found!")
                        break

        print("--------------------------------------------")
        print("Exit Successful!")
        print("All data stored to data.json")


d = Datastore()
print(d.create_account())
if data:
    print(d.inside_acts())
