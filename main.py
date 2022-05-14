
import pandas as pd 

df = pd.read_csv('product_list.csv')

ps = (df.iloc[3])  ##call on this when displaying the ps5s for sale
#print(ps)

ps1 = list(ps)
#print(ps1)


##greeting function 

##gpu function 

##ps5 function 
def sony(greeting,selection,ps5):
    print(greeting)
    for price in selection:
        print(price)
    price_point = ps5
    if price_point == ps1[1]:
        print('PS5 for $%2.f'%ps1[1])
    elif price_point == ps1[2]:
        print('PS5 for $%2.f'%ps1[2])
    elif price_point == ps1[3]:
        print('PS5 for $%2.f'%ps1[3])
    else:
        print('We do not have that price. Sorry')

sony('hi',ps1,750)

#closing function
