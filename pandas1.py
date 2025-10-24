import pandas as pd

RGB = pd.DataFrame({"Red" :[255, 0, 0], "Green" : [0, 255, 0], "Blue" : [0, 0, 255]})
fruit_sales = pd.DataFrame({"Apples" : [35, 41], "Bananas" : [21, 34]}, index = ['2017 Sales', '2018 Sales'])
ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index = ['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')

print(RGB)
print(RGB['Red'])
print(ingredients)
print(fruit_sales)