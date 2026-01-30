empty_tuple = tuple()
sisters = ('Zuly', 'Dayana')
brothers = ('Steven', 'Maxi')
sisters_brothers = sisters + brothers
print(sisters_brothers)
print(len(sisters_brothers))
lst_sisters_brothers = list(sisters_brothers)
lst_sisters_brothers.append('Elsy')
lst_sisters_brothers.append('Reynaldo')
print(lst_sisters_brothers)

siblings = tuple(lst_sisters_brothers[0:4])
print(siblings)
paremts = tuple(lst_sisters_brothers[4:6])
print(paremts)

fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits)
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
print(vegetables)
animal_products = ('milk', 'meat', 'butter', 'yogurt')
print(animal_products)
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
food_stuff_middle = food_stuff_lt[4:7]
print('Middle items:', food_stuff_middle)
first_three = food_stuff_lt[0:3]
print('First three items:', first_three)
last_three = food_stuff_lt[-3:]
print('Last three items:', last_three)
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(nordic_countries)
print('Is Estonia in nordic_countries?', 'Estonia' in nordic_countries)
print('Is Iceland in nordic_countries?', 'Iceland' in nordic_countries)