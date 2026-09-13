'''
Day 23 09/09/26

Building project on ATM
used
MINI Statement
Home Page
Exit

'''


sami_details_ICICI = {
    "Name" : 'sami',
    'Adr' : '1234567890',
    'pan' : 'GPCBU2073T',
    'ATMPIN' : '6600',
    'Balance' : 10000,
    'MINI State': []
}
All_attmps = 3
while All_attmps > 0:
    user_pin = input('Enter a 4 digit pin: ')
    if user_pin in sami_details_ICICI['ATMPIN'] and len(user_pin) ==4:
       print('Welcome ICICI ATM')
       choice_ = int(input('Enter \n1.Withdraw\n2.Deposite\n3.Check Balance: '))
       if choice_ == 1:
            with_m = int(input('Enter amount to withdraw: '))
            if with_m <= sami_details_ICICI['Balance'] and with_m % 100 ==0:
              sami_details_ICICI['Balance'] -= with_m
              print(f'Take your cash and the balance is {sami_details_ICICI["Balance"]}')
              sami_details_ICICI['MINI State'].append(f'Withdraw: {with_m}')
              print(f"{sami_details_ICICI['MINI State']}")
              user_opt = int(input('Enter \n1.Home Page \n2.Exit: '))
              if user_opt == 1:
                  print('Taking to home page')
              elif user_opt == 2:
                  print('Thanks for visiting')
                  break
            else:
                  print('insufficient balance or This ATM can not provide change')
                  break
       elif choice_ == 2:
            depo_m = int(input('Enter amount to deposit: '))
            if depo_m % 100 ==0:
                sami_details_ICICI['Balance'] += depo_m
                print(f' amount to deposit and total amount in your balance is{sami_details_ICICI["Balance"]}')
                sami_details_ICICI['MINI State'].append(f'Deposit: {depo_m}')
                print(f"{sami_details_ICICI['MINI State']}")
                user_opt = int(input('Enter \n1.Home Page \n2.Exit: '))
                if user_opt == 1:
                    print('Taking to home page')
                elif user_opt == 2:
                    print('Thanks for visiting')
                    break
                    
            else:
                print('This ATM is not accepts change')
       elif choice_ == 3:
            print(f'Your balance is {sami_details_ICICI["Balance"]}')
       else:
            All_attmps -= 1
            if All_attmps > 0:
                print(f'Incorrect pin entered and you have {All_attmps} left')
            else:
                print('Your card is blocked..')

