store = 's'
usrName = input('What is your Name? ')
   
store = input(usrName + 'WELCOME TOO MARKET PLUS for the frozen food section type 1, for the canned goods type 2 , for the mens clothes type 3, for the womens clothes type 4, for the tech type 5, for the bakery type 6, for the beauty type 7' ) 

while len(store) > 1 or store.isdigit() == False:
    store = input('TYPE A NUMBER NOW! ')

while int(store) > 7 :
    store = input('TYPE BETWEEN 1-7! ')

frozenFood = ["El monterray burritoes-$5.19" , "Bibigo Mandu Dumplings-$10.49" , "Red Baron Pizza-6.99$" , "Hot Pockets(12pack)-$13.88" , "El monterray taquitos-$9.69" , "Boudin BALLS-$9.89" , "Members mark chiken BREAST-$15.98" , "Blue Bunny Ice cream-$4.48" , "MEGA MEAT BONELESS STRIP OF MEAT-$3.99" , "Mangonada de Hielo-$2.50"] 

cannedGoods = ["Del Monte Green beans-$4.47" , "Del Monte Fresh cut Potatoes-$2.38" , "Del Monet Fiesta Corn-$2.29" , "Del monte Whole Kernel Corn-$2.09" , "Del monte Fruit cocktail-$8.88" , "Del Monte Sliced Peaches-$15.09" , "Del Monte no sugar Very Cherry mixed fruit-$3.79" , "Del Monte Peach Chunks-$2.28" , "Del Monte Fruit Naturals Red GrapeFruit Method-$1.48" , "Del MOnte Lima beans-$2.99"]

mensClothes = ["Hennything is possible Tshirt-$19.99" , "Mens Summer games Cargo pants-$40.00" , "Nordstorm Trim fit Dress shirt-$59.50" , "Brown Jacket-$100.00" , "Nike Sportswear Fullzip hoodie-$130.00" , "Opposuits Men Black suit-$79.00" , "Dirty white shorts-$100" , "Fake beard-1,399.99" , "Mens Wedding shirt-$70.95"]

womensClothes = ["Somerset Maxidress Anthropologie in white-$168" , "Balenciaga Womens flower jersey Cycling dress-$3,190" , "Tu Lize knitted sleeves oversized jacket-$1,086" , "Dior mid lengthe shirt dress yellow silk chiffon multi color pixel zodiac-5,000" , "Womens White Auburn Dress-$433.00" , "Black top with stars-$98" , "Old couch pattern mini dress-"]



