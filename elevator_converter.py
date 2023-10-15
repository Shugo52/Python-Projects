print('This is a code to help convert elevator floors for people in US and EUROPE.')
cont = input('Are you in your continent(yes or no):\n')
if cont == 'yes' or cont == 'Yes' or cont == 'YES':
    floor = input('What floor are you going to:')    
    print('You should input', floor, ' on elevator.')
elif cont == 'no' or cont =='No' or cont == 'NO':
    inp = input('What continent are you in(US or EUROPE):\n')
    if inp == 'US' or inp == 'Us' or inp == 'us':
        floor = input('What floor are you going to:\n')
        print('You should input', floor,' on elevator.')
    elif inp == 'EUROPE' or inp == 'Europe' or inp == 'europe':
        floor = input('What floor are you going to:\n')
        floor = int(floor) - 1
        print('You should input', floor,' on elevator.')