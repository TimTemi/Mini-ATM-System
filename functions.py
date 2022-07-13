import sys


db = {'Tope75': {"name": "Tope Oke", "password": "Topepompin67",
 "email": "topeoke@nhubfondation.org", "contact": "08177509782", "account balance": 10000},
          "Emma419": {"name": "Emmanuel James", "password": "Emmaforthemoney900",
          "email": "emmanueljames@nhubfoundation.org", "contact": "09054799258", "account balance": 50000},
          "Ken_drik": {"name": "Kenneth James", "password": "Kendrick500",
          "email": "kennethjames@nhubfoundation.org", "contact": "07098457234", "account balance": 5000}
             }

print(" Serving Nigeria, One Transaction at a time.\n Press any key to continue....... \n ==> ")
input()
print("\n Welcome to Charis Bank..\n Please Enter your UserName to proceed ")
user_id = input()

def verify_users(user_id):

    if user_id in db:
        return True
    else:
        return False

def register_user():

    print(" Please Fill the form Below to Register as New User\n")
    username = input(" Please Enter UserName ==>    ")
    name = input(" Please Enter your fullname ==>   ")
    passwd = input(" Please Enter your secret password ")

    while any(map(str.isdigit, passwd)) is False or any(map(str.isupper, passwd)) is False or len(passwd) < 9:
            if any(map(str.isdigit, passwd)) is False:
                print(" Password must contain digits!! \n ")
                print(" Please enter your secret password \n  (Password must contain digits, special characters and be at least 9 characters long) \n ==> ")
                passwd = input(" Password:    ")
            elif any(map(str.isupper, passwd)) is False: 
                print(" Password must contain upper case characters !! \n ")
                print(" Please enter your secret password \n  (Password must contain digits, special characters and be at least 9 characters long) \n ==> ")
                passwd = input(" Password:  ")
            elif len(passwd) < 9:
                print(" Password must be at least 9 characters long !! \n ")
                print(" Please enter your secret password \n  (Password must contain digits, special characters and be at least 9 characters long) \n ==> ")
                passwd = input(" Password:   ")

    else:
        pass

    confirmed_password =input("confirm password")
    while confirmed_password != passwd:
                print(' Password Not Matching ')
                confirmed_password = input(' confirm password')
    else:
        pass
    email = input(" Please Enter your Email Address:   ")
    contact = input(" Please Enter your Phone Number:   ")

    db.update({username: {"name": name, "email": email, 
         "contact": contact, "password": passwd, 'account balance':0}})

    print("You have successfully registered!!")

    return username


def verify_pwd(pwd):

    password_lim = 3
    while pwd != db[user_id]["password"]:
        print(f"Password Incorrect...\n Please Try again\n you have {password_lim} attempts left \n")
        print("if you don't wish to try password press X to exit")
        end = input()
        if end == "X":
            sys.exit()
        pwd = input(" Please enter your secret password \n ==> ")
        password_lim -= 1
        if password_lim == 0:
                print("ATM card seized")
                sys.exit()

    else:
        pass  

def transactions_view():
    
    print(" Please select your desired action below \n")
    print(" A: Instant Transfer    B: Mobile Top-up    \n     C: Check Balance   D:Withdrawal   \n ==>  ")
    #action_list = {"A" : "Instant Transfer", "B" : "Airtime Recharge", 
     #"C" : "Withdrawal", "D" : "Check Balance"}
    action = input()
    return action 


def instant_transfer_view(user_id):
    print("please enter your account number")  
    acc = input()
    
    while len(acc) != 10 or acc.isdigit() is False:
        print( " INVALID ACCOUNT NUMBER....please enter the correct account number: \n  ")   
        acc = input()
    else:
        pass
    
    print("please enter amount")
    amt = int(input())

    while amt < 100 or amt > db[user_id]['account balance']:

        if amt < 100:
            print("cannot transfer amount less than #100.......")
            amt = int(input())
        else:
            print("insufficient funds")
            print(" Press 1 to perform another transaction or 2 to quit ")
            action = input()
            if action == "1":
                return transactions_view()

            else:
                sys.exit()

    else:
        pass

    print("enter secret password to complete transaction")
    pwd = input()

    verify_pwd(pwd)

    db[user_id]['account balance'] -= amt

    print(f"Transaction complete......\n your main balance is: {db[user_id]['account balance']}")
    print("press 1 to perform another transaction or press 2 to quit")
    Opt = input()
    if Opt == "1":
        return transactions_view()
    else:
        sys.exit()

def Mobile_Top_up(user_id):

    print("select service provider: A: 9mobile      B: MTN     \nC: Glo      D: Airtel ")
    opt = input()
    if opt in ["A", "B", "C", "D"]:
        print("Maximum amount to recharge: #10,000.00")
        print("please enter amount")
        amt = int(input())
    else:
        pass

    while amt > 10000 or amt > db[user_id]['account balance']:

        if amt > 10000:
            print("Maximum amount: #10,000.00")
            amt = int(input())
        else:
            print("insufficient funds")
            print(" Press 1 to perform another transaction or 2 to quit ")
            action = input()
            if action == "1":
                return transactions_view()

            else:
                sys.exit()
                

    else:
        pass

    print("enter secret password to complete transaction")
    pwd = input()

    verify_pwd(pwd)

    db[user_id]['account balance'] -= amt

    print(f"Transaction complete......\n your main balance is: {db[user_id]['account balance']}")
    print("press 1 to perform another transaction or press 2 to quit")
    Opt = input()
    if Opt == "1":
        return transactions_view()
    else:
        sys.exit()


def check_balance(user_id):

    print("enter secret password to check account balance")
    pwd = input()
    verify_pwd(pwd)
    
    print(f"your main balance is: {db[user_id]['account balance']}")

    print(" Press 1 to perform another transaction or 2 to quit ")
    
    action = input()
    
    if action == "1":
        return transactions_view()

    else:
        sys.exit()

def withdrawal(user_id):  
    print("enter secret password to continue transaction")
    pwd = input()
    verify_pwd(pwd)

    print("select account: A: Savings account      B: Current account")
    opts = input()
    if opts in ["A", "B"]:
       print("enter amount to withdraw (Maximum amount to withdraw at a time is #20,000.00):")      
       
    amt = int(input())

    while amt < 999 or amt > db[user_id]['account balance']:

        if amt < 999:
            print("cannot withdraw amount less than #999.00.......")
            amt = int(input())
        else:
            print("insufficient funds")
            print(" Press 1 to perform another transaction or 2 to quit ")
            action = input()
            if action == "1":
                return transactions_view()

            else:
                sys.exit()

    else:
        pass  
       
    db[user_id]['account balance'] -= amt

    print(f"withdrawal complete......\n your main balance is: {db[user_id]['account balance']}")
    print("press 1 to perform another transaction or press 2 to quit")
    Opt = input()
    if Opt == "1":
        return transactions_view()
    else:
        sys.exit()  
       
       
       
        # if action == "B":
    #     print("Select network provider:\n E: MTN     F: Glo    \n G: 9mobile      H: Airtel") 
    #     action_1 = input()
    #     if action_1 in  ["E","F","G","H"]:
    #         print("select amount: ")
    # else:
    #        pass
    # def withdraw(acc_balance, amount, username):  

    #  if action == "C":
    #     print("select amount:") 
        
    # if action == "D":
    #     print("account balance is:")         
    #sys.exit()
     #choice = action_list[action]
    #return action




user = verify_users(user_id)

while user == False:

    print(" User Does not Exist....\n Press 1 to try again or Press 2 to Register as a new user")

    action = input()

    if action == '1':
        print("Please enter your username \n ")
        name = input()
        user = verify_users(name)

    else:

        user_id = register_user()
        user = verify_users(user_id)

else:
    pass
     
         
print(" Please enter your secret password to continue \n ==> ")
pwd = input()

verify_pwd(pwd)

print(f" Welcome {db[user_id]['name'].split(' ')[0]} to Charis Bank \n ")


choice = transactions_view()

while choice == "A" or choice == "B" or choice == "C" or choice == "D":
    if choice == "A":
        choice = instant_transfer_view(user_id)
     
    elif choice == "B":
        choice = Mobile_Top_up(user_id)

    elif choice == "C":
        choice = check_balance(user_id) 

    elif choice == "D":
        choice = withdrawal(user_id)
       


else:
       sys.exit()



# if action == "A":
#     print(f" To continue with {choice} \n")
#     print( " Bank to transfer: \n A: FLEMMING BANK     D: HOGWARTS BANK \n B: WEST MIDLANDS BANK     E: OTHERS \n C: REVENANT BANK  \n ==>")
#     Banks = dict(A = "FLEMMING BANK", B = "WEST MIDLANDS BANK", C = "REVENANT BANK",
#                     D = "HOGWARTS BANK", E = dict(A = "VIOLET BANK", B = "SPARKLING BANK",
#                      C = "ORANGE BANK",
#                     D = "LTD"))
    
#     bank = input()

#     if bank != "E":
#         bank = Banks[bank]
#         print(f"You Selected {bank}  \n ")
#         print(" DESTINATION ACCOUNT NUMBER: \n ==> ")
#         acc = input()
#         while len(acc) != 10:
#             print( " INVALID ACCOUNT NUMBER....PLEASE CHECK AND TRY AGAIN \n  ")
#             print(" Enter account number ==>  ")
#             acc = input()
#         else:
#             pass

#         print("\n AMOUNT TO TRANSFER ==>   \n")
#         amount = int(input())

#         print(" Please Enter Password to continue: \n Password ==>")
#         pwd = input()
#         while pwd != users[user_id]["password"]:
#             print(" Incorrect Password, Please Try again!! \n")
#             pwd = input()
#             if pwd == users[user_id]["password"]:
#                 print(f" YOU TRANSFERED {amount} TO USER {acc} AT {bank}  ")
#                 break
#             else:
#                 pass
#         print(" Press any key to exit.. \n")
#         input()
#         sys.exit()

#     else:
#         print(" SELECT BANK: \n A: VIOLET BANK        C: ORANGE BANK \n B: SPARKLING BANK        D: LTB \n ==>")
#         other_bank = input()
#         bank = Banks[bank][other_bank]
#         print(f"You Selected {bank}  \n")
#         print(" DESTINATION ACCOUNT NUMBER: \n ==> ")
#         acc = input()
#         while len(acc) != 10:
#             print( " INVALID ACCOUNT NUMBER....PLEASE CHECK AND TRY AGAIN \n  ")
#             print(" Enter account number ==>  ")
#             acc = input()
#         else:
#             pass

#         print("\n AMOUNT TO TRANSFER ==>   \n")
#         amount = int(input())

#         print(" Please Enter Password to continue: \n Password ==>")
#         pwd = input()
#         while pwd != users[user_id]["password"]:
#             print(" Incorrect Password, Please Try again!! \n")
#             pwd = input("==> ")
#             if pwd == users[user_id]["password"]:
#                 print(f" YOU TRANSFERED {amount} TO USER {acc} AT {bank}  ")
#                 break
#         print(" Press any key to exit.. \n")
#         input()
#         sys.exit()

# else:
#     sys.exit()
    
    #  if action ==== "B"
    # printstyled( " Service Provider: \n A: VERIZON    C: REVERE \n B: LOKI     D: MOCA  \n ==>"; color = :green)
    # Providers = Dict("A" => "VERIZON", "B" => "LOKI", "C" => "REVERE", "D" => "MOCA")

    # line = readline()

    # println("Thanks a lot for using our service")
    # clear()