import time
print('Please insert your ATM Card')
time.sleep(3)
print('-----------------------------')
print('We Can Verify Your ATM Card')
time.sleep(4)
pin = int(input('Enter your 4 digit ATM Pin'))
balance = 1000
if pin == 2024:
    while True:
        print("1 = Check Balance")
        print("2 = Withdraw Money")
        print("3 = Deposit Money")
        print("4 = Exit")
        try:
            option = int(input('Choose any option above'))
        except:
            print("Please choose the valid option")
        if option == 1:
            print('----------------------------------')
            print(f'Your current balance is {balance}')
        if option == 2:
            withdraw_money = int(input('Enter the Withdraw Amount'))
            if withdraw_money < balance:
                balance = balance - withdraw_money
                print('----------------------------------')
                print('Be Patients We Are Processing Your Transaction')
                time.sleep(4)
                print(f'{withdraw_money} is debited from your account')
                print(f'Your current balance is {balance}')
            else:
                print('You have insufficient funds')
        if option == 3:
            deposit_money = int(input('Enter the deposit amount'))
            balance = balance + deposit_money
            print('----------------------------------')
            print('Be Patients It can Take few Seconds...')
            time.sleep(4)
            print(f'{deposit_money} is credited to your account')
            print(f'Your current balance is {balance}')
        if option == 4:
            print('Thank you for visiting our ATM Machine...See you Again')
            break

else:
    print('You entered the wrong pin...Try Again')