# aq inaceba is monacemebi romelebic sheva
data = []


def register():
    # მომხმარებლის სახელი
    username = input("Enter your username: ")
    
    # პაროლი
    password = input("Create a new password: ")

    #აქ უნდა შევინახოთ მომხმარებლის მონაცემები
    current_user = {
        "name": username,
        "password": password
    }

    # აქ თუ მომხმარებელი არ არის ჯერ შეყვანილი სიაში 
    if len(data) == 0:
        print("Registration successfull!")
        # მომხმარებელს ვამატებთ სიაში
        data.append(current_user)
    
    # ეს კი თუ უკვე არსებობს ინფორმაცია
    elif len(data) > 0:

 # ვამოწმებთ არსებულ მომხმარებელს 
        for i in data:
            
            # უკვე არსებობს 
            if i["name"] == current_user["name"]:
                print("username already exists!")
                
                # მომხმარებელს თავიდან ვთხოვთ სახელს
                username = input("Enter another username again: ")
                
                # ვუცვლით username-ს current_user-ს
                current_user["name"] = username
                
                # ვამატებთ სიაში
                data.append(current_user)
                
                break
            else:
                print("Registration successfull!")
                # ვამატებთ ახალ მომხმარებელს სიაში
                data.append(current_user)
                break
register()
register()
register()
print(data)