data = []

def register():
    username = input("enter your username:")
    password = input("enter your password:")

    current_user = {
        "name":username,
        "password": password
    }
    if len(data) ==0:
        print("registration succesfull")
        data.append(current_user)


    elif len(data) > 0:
        for i in data:
            if i ["name"]  == current_user["name"]:
                print("username slready exists!")
                username = input("enter ur username again: ")
            else:
                print("registration succesfull!")
                data.append(current_user)
                print(data)


    def login():
        username = input ("enter your username:")
        password = input ("create a new password")

        current_user = {
            "name":username,
            "password":password
        }

        register()