import json
import os
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
print("\n========================================================================================\n")
print("Do you want to register? (Required when installing first time)")
print("Enter Yes to register and any key to continue.")
option = input()
if option.lower() == 'yes':
    user = {"username": "default_user", "password": "password", "preffered_browser": "Firefox",
            "proxy_address": "proxy2.iitj.ac.in/xxxxxxxxxxxxxxxxxxx/172.30.0.56/http://www.msftconnecttest.com/redirect", "win10username": "Administrator"}
    os.system('color 01')
    os.system('@echo off')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print("\n========================================================================================\n")
    os.system('color 02')
    user["username"] = input("Enter your LDAP username: ")
    print("\n========================================================================================\n")
    os.system('color 03')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print("\n========================================================================================\n")
    user["password"] = input("Enter your LDAP password: ")
    os.system('color 04')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print("\n========================================================================================\n")
    print("What is your preffered internet browser (You must have the browser installed on your PC)")
    print("\n========================================================================================\n")
    os.system('color 06')
    while True:
        print("Enter the number your preffered browser corresponds to.")
        print("\n========================================================================================\n")
        print("    1. Firefox (Fastest and tested)")
        print("    2. Chrome (Slow and tested)")
        print("    3. Opera (Not tested)")
        print("\nSupport for other browsers will be added soon!")
        print("\n========================================================================================\n")
        option = input("Enter your choice: ")
        if option == '1':
            user["preffered_browser"] = "Firefox"
            break
        if option == '2':
            user["preffered_browser"] = "Chrome"
            break
        if option == '3':
            user["preffered_browser"] = "Opera"
            break
        else:
            print("Please enter a valid option")
            print(
                "========================================================================================")
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    os.system('color 09')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print("========================================================================================")
    print('''Now copy and paste your LDAP proxy URL over here, make sure you don't include \n'https://' protocol in the URL.Your URL must look something like:\nproxy2.iitj.ac.in/xxxxxxxxxxxxxxxxxxx/172.30.0.56/http://www.msftconnecttest.com/redirect''')
    print("========================================================================================")
    user["proxy_address"] = input()
    os.system('color 0a')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print("========================================================================================")
    print("Enter the Username of your Windows User ")
    print("========================================================================================")

    user["proxy_address"] = input()

    with open('user_config.json', 'w') as f:
        json.dump(user, f)
else:
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
