#Copy your code segments into this file. Please add comments for ease of identifying the parts of the program.

#Dictionary for items to be purchased

produce = {
  "BANANAS": 0.35,
  "APPLES": 1.50,
  "ORANGES": 0.75,
  "STRAWBERRIES": 4.00,
  "GRAPES": 4.00,
  "TOMATOES": 1.50,
  "LETTUCE": 2.50,
  "CARROTS": 1.50,
  "BROCCOLI": 2.50,
  "POTATOES": 0.50,
  "ONIONS": 1.00,
  "BELL PEPPERS": 1.50,
  "AVOCADOS": 2.00,
  "CUCUMBERS": 1.00,
  "SPINACH": 3.00,
  "MANGOES": 3.00,
  "PINEAPPLES": 4.00,
  "WATERMELONS": 5.00,
  "CANTALOUPES": 3.50,
  "BLUEBERRIES": 5.00,
}

produceForPrint = {
  "BANANAS 🍌 (each)": f'$ {0.35}',
  "APPLES 🍎 (each)": f'$ {1.50}',
  "ORANGES 🍊 (each)": f'$ {0.75}',
  "Strawberries 🍓 (per pint)": f'$ {4.00}',
  "Grapes 🍇 (per bunch)": f'$ {4.00}',
  "Tomatoes 🍅 (each)": f'$ {1.50}',
  "Lettuce 🥬 (each head)": f'$ {2.50}',
  "Carrots 🥕 (per bunch)": f'$ {1.50}',
  "Broccoli 🥦 (each)": f'$ {2.50}',
  "Potatoes 🥔 (each)": f'$ {0.50}',
  "Onions 🧅 (each)": f'$ {1.00}',
  "Bell Peppers 🫑 (each)": f'$ {1.50}',
  "Avocados 🥑 (each)": f'$ {2.00}',
  "Cucumbers 🥒 (each)": f'$ {1.00}',
  "Spinach 🍃 (per bunch)": f'$ {3.00}',
  "Mangoes 🥭 (each)": f'$ {3.00}',
  "Pineapples 🍍 (each)": f'$ {4.00}',
  "Watermelons 🍉 (each)": f'$ {5.00}',
  "Cantaloupes 🍈 (each)": f'$ {3.50}',
  "Blueberries 🫐 (per pint)": f'$ {5.00}',
}



beverages = {
  "WATER": 1.50,
  "SODA": 1.25,
  "COFFEE": 4.00,
  "TEA": 4.50,
  "ORANGE JUICE": 4.00,
  "ICED TEA": 3.00,
  "ENERGY DRINK": 4.00,
  "SMOOTHIE": 6.00,
  "LEMONADE": 2.50,
  "COCONUT WATER": 3.50,
  "JUICE BOX": 1.00,
  "ICED COFFEE": 4.00,
  "WINE": 15.00,
  "BEER": 10.00,
  "HOT CHOCOLATE": 3.50,
}




beveragesForPrint = {
  "Water 💧 (per bottle)": f'$ {1.50}',
  "Soda 🥤 (per can)": f'$ {1.25}',
  "Coffee ☕ (per cup)": f'$ {4.00}',
  "Tea 🍵 (per box)": f'$ {4.50}',
  "Orange Juice 🍊 (per bottle)": f'$ {4.00}',
  "Iced Tea 🧊🍵 (per bottle)": f'$ {3.00}',
  "Energy Drink ⚡ (per can)": f'$ {4.00}',
  "Smoothie 🥤 (per cup)": f'$ {6.00}',
  "Lemonade 🍋 (per bottle)": f'$ {2.50}',
  "Coconut Water 🥥💧 (per bottle)": f'$ {3.50}',
  "Juice Box 🧃 (per carton)": f'$ {1.00}',
  "Iced Coffee 🧊☕ (per bottle)": f'$ {4.00}',
  "Wine 🍷 (per bottle)": f'$ {15.00}',
  "Beer 🍺 (per six-pack)": f'$ {10.00}',
  "Hot Chocolate ☕🍫 (per cup)": f'$ {3.50}',
}


bakery = {
  "BREAD": 3.50,
  "BAGUETTE": 2.50,
  "CROISSANTS": 8.00,
  "CUPCAKES": 5.00,
  "MOON CAKES": 3.50,
  "COOKIES": 6.00,
  "CUSTARDS": 5.00,
  "DONUTS": 2.00,
  "PIES": 12.00,
  "CAKES": 5.00,
  "BAGELS": 6.00,
  "PRETZELS": 1.50
}


bakeryForPrint = {
  "Bread 🍞 (per loaf)": f'$ {3.50}',
  "Baguette 🥖 (each)": f'$ {2.50}',
  "Croissants 🥐 (per dozen)": f'$ {8.00}',
  "CupCakes 🧁 (per pack)": f'$ {5.00}',
  "Moon Cakes 🥮 (per pack)": f'$ {3.50}',
  "Cookies 🍪 (per dozen)": f'$ {6.00}',
  "Custards 🍮 (each)": f'$ {5.00}',
  "Donuts 🍩 (each)": f'$ {2.00}',
  "Pies 🥧 (each)": f'$ {12.00}',
  "Cakes 🎂 (per slice)": f'$ {5.00}',
  "Bagels 🥯 (per dozen)": f'$ {6.00}',
  "Pretzels 🥨 (each)": f'$ {1.50}'
}


dairy = {
  "MILK": 4.50,
  "BUTTER": 4.00,
  "CHEESE": 6.00,
  "CHOCOLATE MILK": 4.50,
  "EGGS": 3.00,
  "YOGURT": 2.50,
  "SOUR CREAM": 2.50,
}


dairyForPrint = {
  "Milk 🥛 (per gallon)": f'$ {4.50}',
  "Butter 🧈 (per pound)": f'$ {4.00}',
  "Cheese 🧀 (per pound)": f'$ {6.00}',
  "Chocolate Milk 🍫🥛 (per gallon)": f'$ {4.50}',
  "Eggs 🥚 (per dozen)": f'$ {3.00}',
  "Yogurt 🥣 (per container)": f'$ {2.50}',
  "Sour Cream 🍶 (per container)": f'$ {2.50}',
}

deli = {
  "CHICKEN BREAST": 5.00,
  "GROUND BEEF": 6.00,
  "PORK CHOPS": 5.50,
  "SUSHI": 12.00,
  "TURKEY": 4.50,
  "LAMB CHOPS": 12.00,
  "BACON": 7.00,
  "GROUND TURKEY": 5.00,
  "BEEF TENDERLOIN": 15.00,
  "PORK RIBS": 7.00,
  "SHRIMP": 15.00,
  "BEEF SIRLOIN": 9.00,
  "HAM": 5.00,
  "CHICKEN THIGHS": 4.00,
  "VEAL CUTLETS": 14.00,
  "CANNED TUNA": 3.00,
  "HOT DOGS": 4.00,
}


deliForPrint = {
  "Chicken Breast 🍗 (per pound)": f'$ {5.00}',
  "Ground Beef 🥩 (per pound)": f'$ {6.00}',
  "Pork Chops 🐖 (per pound)": f'$ {5.50}',
  "Sushi 🍣 (per pack)": f'$ {12.00}',
  "Turkey 🦃 (per pound)": f'$ {4.50}',
  "Lamb Chops 🐑 (per pound)": f'$ {12.00}',
  "Bacon 🥓 (per pound)": f'$ {7.00}',
  "Ground Turkey 🦃 (per pound)": f'$ {5.00}',
  "Beef Tenderloin 🥩 (per pound)": f'$ {15.00}',
  "Pork Ribs 🐖 (per pound)": f'$ {7.00}',
  "Shrimp 🦐 (per pound)": f'$ {15.00}',
  "Beef Sirloin  🥩 (per pound)": f'$ {9.00}',
  "Ham 🐖 (per pound)": f'$ {5.00}',
  "Chicken Thighs 🍗 (per pound)": f'$ {4.00}',
  "Veal Cutlets 🐄 (per pound)": f'$ {14.00}',
  "Canned Tuna 🐟 (per can)": f'$ {3.00}',
  "Hot Dogs 🌭 (per pack)": f'$ {4.00}',
}

snacks = {
  "POTATO CHIPS": 3.50,
  "POPCORN": 2.50,
  "PRETZELS": 3.00,
  "TRAIL MIX": 5.00,
  "NUTS": 6.00,
  "CHOCOLATE": 2.50,
  "CRACKERS": 3.50,
  "RICE CRACKER": 4.00,
  "SALSA": 3.50,
  "BEEF JERKY": 7.00,
}



snacksForPrint = {
  "Potato Chips 🥔 (per bag)": f'$ {3.50}',
  "Popcorn 🍿 (per bag)": f'$ {2.50}',
  "Pretzels 🥨 (per bag)": f'$ {3.00}',
  "Trail Mix 🥜 (per bag)": f'$ {5.00}',
  "Nuts 🥜 (per pack)": f'$ {6.00}',
  "Chocolate 🍫 (per bar)": f'$ {2.50}',
  "Crackers 🍪 (per box)": f'$ {3.50}',
  "Rice Cracker 🍘 (per pack)": f'$ {4.00}',
  "Salsa 🍅🌶️ (per jar)": f'$ {3.50}',
  "Beef Jerky 🐄 (per pack)": f'$ {7.00}',
}


frozen = {
  "FROZEN PIZZA": 8.00,
  "FROZEN BROCCOLI": 3.00,
  "ICE CREAM": 5.00,
  "FROZEN CHICKEN NUGGETS": 5.00,
  "FROZEN FRENCH FRIES": 3.50,
  "FROZEN BURRITOS": 4.50,
  "FROZEN STRAWBERRIES": 4.00,
  "FROZEN SHRIMP": 10.00,
  "FROZEN DINNERS": 5.00,
  "FROZEN WAFFLES": 3.50,
  "FROZEN CHICKEN WINGS": 8.00,
  "FROZEN DUMPLINGS": 6.00,
}


frozenForPrint = {
  "Frozen Pizza 🍕 (per box)": f'$ {8.00}',
  "Frozen Broccoli 🥦 (per bag)": f'$ {3.00}',
  "Ice Cream 🍨 (per pint)": f'$ {5.00}',
  "Frozen Chicken Nuggets 🍗 (per bag)": f'$ {5.00}',
  "Frozen French Fries 🍟 (per bag)": f'$ {3.50}',
  "Frozen Burritos 🌯 (per pack)": f'$ {4.50}',
  "Frozen Strawberries 🍓 (per bag)": f'$ {4.00}',
  "Frozen Shrimp 🦐 (per bag)": f'$ {10.00}',
  "Frozen Dinners 🍽️ (per meal)": f'$ {5.00}',
  "Frozen Waffles 🧇 (per box)": f'$ {3.50}',
  "Frozen Chicken Wings 🍗 (per bag)": f'$ {8.00}',
  "Frozen Dumplings 🥟 (per bag)": f'$ {6.00}',
}

aisles = {
    "PRODUCE": produceForPrint,
    "BEVERAGES": beveragesForPrint,
    "BAKERY": bakeryForPrint,
    "DAIRY": dairyForPrint,
    "DELI": deliForPrint,
    "SNACKS": snacksForPrint,
    "FROZEN": frozenForPrint
}

shoppingCart = {}



#Display the Catalog to the User

print("Welcome to the Grocery Store.\n")

while True:
  promptAisle = input("What aisle would you like to go to? Produce, Beverages, Bakery, Dairy, Deli, Snacks, or Frozen. Enter: ").upper()

  if promptAisle in aisles:
    print(f'\nThis is the {promptAisle.lower()} aisle.')
    for key, val in aisles[promptAisle].items():
      print(key, val)
    break
  else:
    print('\nSorry we dont have that aisle, or you spelled the aisle wrong.\n')


