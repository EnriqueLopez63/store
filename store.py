from multiprocessing.sharedctypes import Value


def storeMeth():
    store = 's'
    usrName = input('What is your Name? ')
    



    cont  = ("y")


    frozenFood1 = {'ElMonterrayBurritoes':5.19 , 'Bibigo Mandu Dumplings' : 10.49 , 'Red Baron Pizza' : 6.99 , 'Hot Pockets(12pack)':13.88 , 'El monterray taquitos': 9.69 , 'Boudin BALLS':9.89 , 'Members mark chiken BREAST':15.98, 'Blue Bunny Ice cream':4.48 , 'MEGA MEAT BONELESS STRIP OF MEAT':3.99, 'Mangonada de Hielo':2.50}


    cannedGoods2 = {'Del Monte Green beans':4.47 , 'Del Monte Fresh cut Potatoes':2.38 , 'Del Monet Fiesta Corn':2.29 , 'Del monte Whole Kernel Corn':2.09 , 'Del monte Fruit cocktail':8.88 , 'Del Monte Sliced Peaches':15.09 , 'Del Monte no sugar Very Cherry mixed fruit':3.79 , 'Del Monte Peach Chunks':2.28 , 'Del Monte Fruit Naturals Red GrapeFruit Method':1.48 , 'Del MOnte Lima beans':2.99}

    mensClothes3 = {'Hennything is possible Tshirt':19.99 , 'Mens Summer games Cargo pant':40.00 , 'Nordstorm Trim fit Dress shirt':59.50 , 'Brown Jacket':100.00 , 'Nike Sportswear Fullzip hoodie':130.00 , 'Opposuits Men Black suit':79.00 , 'Dirty white shorts':100 , 'Fake beard':1399.99 , 'Mens Wedding shirt':70.95}

    womensClothes4 = {'Somerset Maxidress Anthropologie in white':168 , 'Balenciaga Womens flower jersey Cycling dressL':3190 , 'Tu Lize knitted sleeves oversized jacket':1086 , 'Dior mid lengthe shirt dress yellow silk chiffon multi color pixel zodiac':5000 , 'Womens White Auburn Dress':433.00 , 'Black top with stars':98 , 'Old couch pattern mini dress':75.99}

    tech5 = {'Meta Quest 2 Vr':399.99  , 'Acer Swift laptop':1099.99 , 'Flagship chromebook':94.99, "Google pixel 6a-$369.99" , "Samsung Galaxy A10e-$102.99" , "Iphone 11pro-$524.95" , "Intel i7cpu-$321.97" , "Hp pavillio32-$2,399.99" , "Lphone 10-$5" , "Samsung odyysey ark monitor-$3,499.99"]

    bakery6 = ["GlazedDonut-$.99" , "ChocolateDonut-$.99" , "LoafofBread-$4.50" , "Sugar poudered poudered sugar that is poudered donuts-$41.97" , "ChocolateChipCookie-$1.25" , "SugarCookie-$1"
    , "Brownie-$1.25" , "Pizza-$12" , "Cake-$9" , "Cupcake-$.75"]

    beauty7 = ["red lipstick-$7" , "BlueLipstick-$5" , "orangeLipstick-$4" , "pinkLipstick-7" , "Mascara-$20" , "LashExtensions-$15" , "NoseSurgery-$5,000" , "greenWig-$25" , "deoderant-$2" "Shampoo-$10"] 

    while (cont == "y"):

        store = input(usrName + 'WELCOME TOO MARKET PLUS for the frozen food section type 1, for the canned goods type 2 , for the mens clothes type 3, for the womens clothes type 4, for the tech type 5, for the bakery type 6, for the beauty type 7. ' ) 

        while len(store) > 1 or store.isdigit() == False:
            store = input('TYPE A NUMBER NOW! ')

        while int(store) > 7 :
            store = input('TYPE BETWEEN 1-7! ')

        if int(store) == 1:
            for item , value in frozenFood1.items():
                print(item , value)


        elif int(store) == 2:
            for item , value2 in cannedGoods2.items():
                print(item , value2)


        elif int(store) == 3:
            for item in mensClothes3:
                print(item)


        elif int(store) == 4:
            for item in womensClothes4:
                print(item)


        elif int(store) == 5:
            for item in tech5:
                print(item)

        elif int(store) == 6:
            print(bakery6)

        elif int(store) == 7:
            print(beauty7)

        inue = input("would you like to visit another section please type y or n")
        while inue != "y" and inue != "n":
            inue = input("Would you like to visit another section please type y or n")
        if inue == "y":
            cont = "y"
        elif inue == "n":
            cont = "n"
            


