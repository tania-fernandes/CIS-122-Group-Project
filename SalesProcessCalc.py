#Copy your code segments into this file. Please add comments for ease of identifying the parts of the program.

#Dictionary for items to be purchased

produce = {
  "Bananas 🍌 (each):": f'$ {0.35}',
  "Apples 🍎 (each)": f'$ {1.50}',
  "Oranges 🍊 (each)": f'$ {0.75}',
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
  "Milk 🥛 (per gallon)": f'$ {4.50}',
  "Butter 🧈 (per pound)": f'$ {4.00}',
  "Cheese 🧀 (per pound)": f'$ {6.00}',
  "Chocolate Milk 🍫🥛 (per gallon)": f'$ {4.50}',
  "Eggs 🥚 (per dozen)": f'$ {3.00}',
  "Yogurt 🥣 (per container)": f'$ {2.50}',
  "Sour Cream 🍶 (per container)": f'$ {2.50}',
}

deli = {
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
    "PRODUCE": produce,
    "BEVERAGES": beverages,
    "BAKERY": bakery,
    "DAIRY": dairy,
    "DELI": deli,
    "SNACKS": snacks,
    "FROZEN": frozen
}



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
    print('\nSorry we don't have that aisle.\n')

