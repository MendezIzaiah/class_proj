
import pandas as pd 

df = pd.read_csv('product_list.csv')

ps = (df.iloc[3])  ##call on this when displaying the ps5s for sale
#print(ps)

ps1 = list(ps)
#print(ps1)


##greeting function 

##gpu function 
contloop = 'Continue'
xyz = ''
##while loop sentinal values for gpu function

psjall = (df.iloc[0:3])
psj1 = (df.iloc[0])
psj2 = (df.iloc[1])
psj3 = (df.iloc[2])
##data gram print variables 



    
def gpu_options(greeting,seller_choice,gpu):
    xyz = 'poop'
    while xyz != contloop:
        print(greeting)
        print(psjall)
        gpupick = gpu
        if gpupick == "None":
            print("Goodbye")
        elif gpupick == "GPU 3060":
            print('Pick a seller!\n')
            print(psj1)
            seller_choice = input()
            if seller_choice == 'Seller 1':
                print("GPU 3060's",'$%2.f'%500,"Enjoy your GPU 3060!" )
                xyz = 'Continue'
            elif seller_choice == 'Seller 2':
                print("GPU 3060's",'$%2.f'%650,"Enjoy your GPU 3060!" )
                xyz = 'Continue'
            elif seller_choice == 'Seller 3':
                print("GPU 3060's",'$%2.f'%600,"Enjoy your GPU 3060!" )
                xyz = 'Continue'
            else:   
                print('Please select a valid Seller!')
                seller_choice = input()
                
        elif gpupick == "GPU 3080":
            print('Pick a seller!\n')
            print(psj2)
            seller_choice2 = input()
            if seller_choice2 == 'Seller 1':
                print("GPU 3080's",'$%2.f'%1200,"Enjoy your GPU 3080!" )
                xyz = 'Continue'
            elif seller_choice2 == 'Seller 2':
                print("GPU 3080's",'$%2.f'%1100,"Enjoy your GPU 3080!" )
                xyz = 'Continue'
            elif seller_choice2 == 'Seller 3':
                print("GPU 3080's",'$%2.f'%1350,"Enjoy your GPU 3080!" )
                xyz = 'Continue'
            else:   
                print('Please select a valid Seller!')
                seller_choice2 = input()
                
                
        elif gpupick == "GPU 3090":
            print('Pick a seller!\n')
            print(psj3)
            seller_choice3 = input()
            if seller_choice3 == 'Seller 1':
                print("GPU 3090's",'$%2.f'%2000,"Enjoy your GPU 3090!" )
                xyz = 'Continue'
            elif seller_choice3 == 'Seller 2':
                print("GPU 3090's",'$%2.f'%2100,"Enjoy your GPU 3090!" )
                xyz = 'Continue'
            elif seller_choice3 == 'Seller 3':
                print("GPU 3090's",'$%2.f'%2150,"Enjoy your GPU 3090!" )
                xyz = 'Continue'
            else:   
                print('Please select a valid Seller!')
                seller_choice3 = input()
                
        else:
            print('Please select a valid GPU!')
            gpupick = input()


#gpu_options('Welcome to the GPU store','something','GPU 3060')


##ps5 function 
def sony(greeting,selection,ps5):
    print(greeting)
    counter = 1
    for price in selection[1:]:
        print(f'Seller {counter} for $', price)
        counter += 1
    price_point = ps5 #might have to make an input statement 
    if price_point == ps1[1]:
        print('PS5 for $%2.f'%ps1[1])
    elif price_point == ps1[2]:
        print('PS5 for $%2.f'%ps1[2])
    elif price_point == ps1[3]:
        print('PS5 for $%2.f'%ps1[3])
    else:
        print('We do not have that price. Sorry')

#sony('hi',ps1,750)

#closing function
def closing(pickeditems,price,goodbye):
    print("Your total of",pickeditems,"is $"+str(price))
    more = input("Would you like to choose a different item (y/n)?")
    if more == "y":
        greet_user("Great!", "No", "What category would you like to browse (GPUs, PS5s)? ", "Ready to browse (y/n)? ")
    elif more == 'n':
        for l in goodbye:
            print(l)
    else:
        more = input('Not a valid response. Continue?(y/n)? ')

        

##closing('PS5','750','goodbye')


