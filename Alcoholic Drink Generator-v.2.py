recipes =[["Lime Marg", "ice", "tequila blanco","lime juice", "sweet n sour", "triple sec"],
          
          ["Strawberry Marg", "ice", "tequila repesado", "lime juice", "strawberry puree", "sweet n sour", "triple sec"],

          ["Mango Marg", "ice", "tequila repesado", "lime juice", "sweet n sour", "mango puree", "triple sec"],

          ["Gin & Tonic", "ice", "gin", "tonic water", "lemon"],

          ["Old Fashioned", "ice", "burbon", "sugar cube", "bitters"],

          ["Texas Marg", "ice", "tequila repesado", "lime juice", "sweet n sour", "grand marnier", "triple sec"],

          ["Horse's Neck ", "ice", "brandy", "ginger ale", "lemon"],

          ["Lemon Drop", "vodka", "lemon", "triple sec"],

          ["Whiskey Sour", "ice", "whiskey", "lemon", "sugar cube"],

          ["Manhattan", "ice", "whiskey", "vermouth", "bitters"],

          ["Negroni", "gin", "vermouth", "campari"],

          ["Moscow Mule", "ice", "vodka", "lime juice", "ginger beer"],

          ["Martini", "vodka", "lemon", "vermouth", "olive"],

          ["Tom Collins", "ice", "gin", "lemon", "soda water"],


          ["Mojito", "ice", "rum", "lime juice", "soda water", "lemon", "mint"]]


          
ingredients = []




print("Welcome to Alcoholic Drink Generator!")

print("Please enter the ingredients you have on hand(type stop to stop input)")

ingredientInput = ""
loopCounter = 1
while ingredientInput != "stop":
    ingredientInput = input("Ingredient # "+str(loopCounter)+":")
    if ingredientInput == "stop":
        break

    ingredients.append(ingredientInput.lower())
    loopCounter = loopCounter + 1

print("Ingredients entered:"+str(ingredients))

completeRecipes = []



numberOfIngredients = 0
for recipe in recipes:
    for recipeIngredient in recipe:
        if recipeIngredient in ingredients:
            numberOfIngredients = numberOfIngredients + 1
            
    if numberOfIngredients == len(recipe)-1:
        completeRecipes.append(recipe)


print("These are the complete drink recipes you can make: "+str(completeRecipes))


print("These are the recipes you are almost able to make")
almostCompleteRecipes = []
missingIngredients = []
numMissing = 0

for recipe in recipes:
    numMissing = 0
    missingIngredients = []
    for recipeIngredient in recipe:
        if recipeIngredient not in ingredients:
            numMissing = numMissing + 1
            missingIngredients.append(recipeIngredient)
            
    if numMissing >1:
        print(missingIngredients.pop(0)+" Shopping List:")

        for missingIng in missingIngredients:
            print("- " + missingIng)

print("Thank you for using Alcoholic Drink Generator v.2!!!!!")




