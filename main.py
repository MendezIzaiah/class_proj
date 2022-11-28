import pandas as pd
import sys 
from appJar import gui
import time 
import math
from datetime import date
from datetime import datetime

start = time.time()

class DevNull:
    def write(self, msg):
        pass

def pooping():
    sys.stderr = DevNull()
    print('\n')
    exit()


#event function
def press(button):
    if button == "Cancel":
        app.stop()
    elif button == "PS5s":
        sony("Welcome to our PlayStation console department! Our selections range from the following:", ps1, "Which is the most optimal price point? ")
    elif button == "GPUs":
        gpu_options("Welcome to our GPU department! Our selections range from the following:", gp, 'Which GPU would you like to buy?')
    else:
        print('Pick a valid option')

#creating GUI variable, appearance 
app = gui("Storefront", "500x500")
app.setBg("blue") #background
app.addImage("decor","vid.gif")
app.setFont(18)

# add & configure widgets - 
app.addLabel("title", "Welcome to Bottom Feeders Emporium")
app.setLabelBg("title", "Black") #title background color
app.setLabelFg("title", "white") #letter color

# link the buttons to the function called press
app.addButtons(["PS5s", "GPUs"], press)
app.addButton('Cancel', press)


df = pd.read_csv('product_list.csv')

ps = (df.iloc[3])  ##call on this when displaying the ps5s for sale
#print(ps)

ps1 = list(ps)
#print(ps1)
gp = (df.iloc[0:3])

##greeting function 
name_sentinel = ' '

name = ' '
def greeting(greet, sentinel, categoryq, readyq):
    global name_sentinel
    global name 
    if name_sentinel == 'y':
        greet = ("Welcome to our store, "+name+"!")
    else:
        name = input("Hey there, what's your name?")
        greet = ("Welcome to our store, "+name+"!")
        name_sentinel = 'y'

    
    #name = input("Hey there, what's your name?")
    #greet = "Welcome to our store, "+name+"!"
    n = 0
    canswer = ' '
    ranswer = sentinel
    print(greet)

    sentinel_app = ' '
    if sentinel_app == 'y':
        sentinel_app = 'placeholder'
    else:
        app.go()
        sentinel_app = 'y'


    while ranswer == sentinel:
        canswer = input(categoryq)
        ranswer = input(readyq)
    
    if canswer.lower() == 'gpu' or canswer.lower()== 'gpus':
        #gpu_options('Welcome to the GPU store','something','GPU 3060')
        gpu_options("Welcome to our GPU department! Our selections range from the following:", gp, 'Which GPU would you like to buy?')
        n = 3
    
    elif canswer.lower() == "ps5" or canswer.lower() == "ps5s":
        n = 3
        sony("Welcome to our PlayStation console department! Our selections range from the following:", ps1, "Which is the most optimal price point? ")
        # ps5 = input("Which PS5 would you like to purchase? ")
        
    
    while ((canswer != "GPU") & (canswer != "PS5") & (n < 1)):
        canswer = input("Invalid input!!! GPU or PS5??")
        n = int(n)
        n = n + 1
        if n == 1:
            print("Okay, have a nice day "+name+"!")      


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
    xyz = 'holder'
    while xyz != contloop:
        print(greeting)
        print(psjall)
        gpupick = input(gpu)
        if gpupick == "None":
            print("Goodbye")
        elif gpupick == "GPU 3060" or gpupick == "gpu 3060" or gpupick == "3060":
            print('Pick a seller!\n')
            print(psj1.to_string(),'\n')
            seller_choice = input(gpu)
            if seller_choice == 'Seller 1':
                closing("GPU 3060's",'$%2.f'%500,"Enjoy" )
                xyz = 'Continue'
            elif seller_choice == 'Seller 2':
                closing("GPU 3060's",'$%2.f'%650,"Enjoy" )
                xyz = 'Continue'
            elif seller_choice == 'Seller 3':
                closing("GPU 3060's",'$%2.f'%600,"Enjoy" )
                xyz = 'Continue'
            else:   
                print('Please select a valid Seller!')
                seller_choice = input(gpu)
                
        elif gpupick == "GPU 3080" or gpupick == "gpu 3080" or gpupick == "3080":
            print('Pick a seller!\n')
            print(psj2.to_string(),'\n')
            seller_choice2 = input()
            if seller_choice2 == 'Seller 1':
                closing("GPU 3080's",'$%2.f'%1200,"Enjoy" )
                xyz = 'Continue'
            elif seller_choice2 == 'Seller 2':
                closing("GPU 3080's",'$%2.f'%1100,"Enjoy" )
                xyz = 'Continue'
            elif seller_choice2 == 'Seller 3':
                closing("GPU 3080's",'$%2.f'%1350,"Enjoy" )
                xyz = 'Continue'
            else:   
                print('Please select a valid Seller!')
                seller_choice2 = input()
                
                
        elif gpupick == "GPU 3090" or gpupick == "gpu 3090" or gpupick == "3090": 
            print('Pick a seller!\n') 
            print(psj3.to_string(),'\n')
            seller_choice3 = input()
            if seller_choice3 == 'Seller 1':
                closing("GPU 3090's",'$%2.f'%2000,"Enjoy" )
                xyz = 'Continue'
            elif seller_choice3 == 'Seller 2':
                closing("GPU 3090's",'$%2.f'%2100,"Enjoy" )
                xyz = 'Continue'
            elif seller_choice3 == 'Seller 3':
                closing("GPU 3090's",'$%2.f'%2150,"Enjoy" )
                xyz = 'Continue'
            else:   
                print('Please select a valid Seller!')
                seller_choice3 = input()
                
        else:
            print('Please select a valid GPU!')
            gpupick = input()


##ps5 function 
def sony(greeting,selection,ps5):
    print(greeting)
    counter = 1
    for price in selection[1:]:
        print(f'Seller {counter} for $', price)
        counter += 1
    ps5_input = str(input(ps5))
    while True:
        if ps5_input == '750' or ps5_input.lower() == 'seller 1' or ps5_input == '1':
            closing('PS5','$%2.f '%ps1[1],'enjoy')
        elif ps5_input == '800' or ps5_input.lower() == 'seller 2' or ps5_input == '2':
            closing('PS5','$%2.f '%ps1[2],'enjoy')
        elif ps5_input == '850' or ps5_input.lower() == 'seller 3' or ps5_input == '3':
            closing('PS5','$%2.f '%ps1[3],'enjoy')
        else:
            ps5_input = input('We do not have that price sorry. Please pick a valid price.')


#closing function
def closing(pickeditems,price,goodbye):
    print("Your total of",pickeditems,"is "+str(price))
    more = input("Would you like to choose a different item (y/n)?")

    while True:
        if more == 'y':
            greeting("Great!", "No", "What category would you like to browse (GPUs, PS5s)? ", "Ready to browse (y/n)? ")
        elif more == 'n':
            for l in goodbye:
                print(l)
            #break
            end = time.time()
            global start
            elapsed = (end-start)
            print('time elapsed is: %.2f seconds' %elapsed)
            break
        else:
            more = input('Not a valid response. Continue?(y/n)? ')
    pooping()
    
    
   
    
greeting("Welcome to our store", "n", "What category would you like to browse (GPUs, PS5s)? ", "Ready to browse (y/n)? ")




