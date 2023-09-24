from tkinter import *

# Readlines for list of food
food = open("foodList", 'r')
x = food.readlines()
food.close

# Readlines for Recipe list
recipes = open("recipes",'r')
y = recipes.readlines()
recipes.close

# Empty lists for appending food a recipes to
foodLst = []
recipesLst = []

# Strips the newline from each list element
for i in range(len(x)):
    foodLst.append(x[i].strip('\n'))
for i in range(len(y)):
    recipesLst.append(y[i].strip('\n'))
    
def organizeLst(header,section):
    '''
    Takes the header of each food storage location in the food list file and
    the section that it is in.

    This function separates each food storage location into its own individual list
    and returns the list.
    '''
    lst = []
    for i in range(len(foodLst)):
        if foodLst[i] == header:
            for n in range(foodLst.index(header) + 1,foodLst.index('-'*section)):
                lst.append(foodLst[n])
    return lst



def displayFood():
    '''
    Runs when the display food button is pressed.

    Displays food available and then opens an entry box where new food to be
    added can be inserted.
    Two buttons are also displayed, one to put the food entred into the 
    box into the cupboard section adn one for the fridge section.
    '''
    food = open("foodList", 'r')
    x = food.readlines()
    food.close

    foodLst = []

    for i in range(len(x)):
        foodLst.append(x[i].strip('\n'))

    for i in range(len(foodLst)-1):
        if foodLst[i] == '-':
            items = []
            x = i + 1
            while foodLst[x+1] != '-':
                items.append(str(foodLst[x+1]) + ',')
                x += 1
            area = Label(root, text=foodLst[i+1])
            foodLabel = Label(root, text=items)
            area.pack()
            foodLabel.pack()

    foodInput = Entry()
    foodInput.pack()

    def addCupboard():
        '''
        Writes the new food inserted into the entry box into the first line
        after the heading 'Cupboards:' and saves the text file.
        '''
        with open('foodList', 'r+') as food:
            contents = food.readlines()
            if "Cupboards:" in contents[-1]:  # Handle last line to prevent IndexError
                contents.append(foodInput.get() + "\n")
            else:
                for index, line in enumerate(contents):
                    if "Cupboards:" in line and foodInput.get() not in contents[index + 1]:
                        contents.insert(index + 1, foodInput.get() + "\n")
                        break
            food.seek(0)
            food.writelines(contents)
        foodInput.delete(0,END)
    def addFridge():
        '''
        Writes the new food inserted into the entry box into the first line
        after the heading 'Fridge:' and saves the text file.
        '''
        with open('foodList', 'r+') as food:
            contents = food.readlines()
            if "Fridge:" in contents[-1]:  # Handle last line to prevent IndexError
                contents.append(foodInput.get() + "\n")
            else:
                for index, line in enumerate(contents):
                    if "Fridge:" in line and foodInput.get() not in contents[index + 1]:
                        contents.insert(index + 1, foodInput.get() + "\n")
                        break
            food.seek(0)
            food.writelines(contents)
        foodInput.delete(0,END)
    
    addFoodCup = Button(root, text="Add Food to Cupboard", command=addCupboard)
    addFoodFridge = Button(root, text="Add Food to Fridge", command=addFridge)
    addFoodCup.pack()
    addFoodFridge.pack()


def displayRecipes():
    '''
    Runs when display recipes button is pressed.

    displays the name of the recipe and the ingredients required to cook it.

    diplays entry box where a new recipe title, and ingredients can be added
    to the recipes list.
    '''
    recipes = open("recipes",'r')
    y = recipes.readlines()
    recipes.close

    recipesLst = []

    for i in range(len(y)):
        recipesLst.append(y[i].strip('\n'))
    
    for i in range(len(recipesLst)-1):
        if recipesLst[i] == '-':
            items = []
            x = i + 1
            while recipesLst[x+1] != '-':
                items.append(str(recipesLst[x+1]) + ',')
                x += 1
            area = Label(root, text=recipesLst[i+1])
            recipesLabel = Label(root, text=items)
            area.pack()
            recipesLabel.pack()
    
    newRecipe = Entry()
    newRecipe.pack()

    def addRecipe():
        with open('recipes','a') as rp:
            rp.write('\n')
            rp.write(newRecipe.get()+':')
        newRecipe.delete(0,END)
    def addIngredient():
        with open('recipes','a') as rp:
            rp.write('\n')
            rp.write(newRecipe.get())
        newRecipe.delete(0,END)
    def addFinalIngredient():
        with open('recipes','a') as rp:
            rp.write('\n')
            rp.write(newRecipe.get())
            rp.write('\n-')
        newRecipe.delete(0,END)

    addRecipeBut = Button(root, text='Add New Recipe', command=addRecipe)
    addIngredientBut = Button(root, text="Add Ingredient", command=addIngredient)
    addFinalIngredientBut = Button(root, text='Add FINAL Ingredient', command=addFinalIngredient)
    addRecipeBut.pack()
    addIngredientBut.pack()
    addFinalIngredientBut.pack()



def displayMeals():
    '''
    Runs when the display meals button is pressed.

    Compares ingredients required for meals to the ingredients in
    the foodList file. If a they match, it prints a label saying which meal
    can be made, and the two other lables showing which ingredients are requred for the meal.
    '''
    recipes = open("recipes",'r')
    y = recipes.readlines()
    recipes.close

    recipesLst = []

    for i in range(len(y)):
        recipesLst.append(y[i].strip('\n'))

    for i in range(len(recipesLst)-1):
        if recipesLst[i] == '-':
            ingredients = []
            x = i + 1
            while recipesLst[x] != '-':
                ingredients.append(recipesLst[x+1])
                x += 1
            if all(elem in foodLst for elem in ingredients):
                mtext = "You have the ingredients to cook " + recipesLst[i+1].strip(":") + "!"
                m = Label(root, text=mtext)
                m.pack()
                ingredients.pop()
                q = Label(root, text="Ingredients Required:")
                r = Label(root, text=ingredients)
                q.pack()
                r.pack()


root = Tk()

# Title widget for the program
title = Label(root, text="Welcome to the Meal Detector!")
desc = Label(root, text="Start by selecting any of the options below.")
# Buttons
foodBut = Button(root, text="Display Food", command=displayFood)
recipeBut = Button(root, text="Display Recipes", command=displayRecipes)
mealBut = Button(root, text="Display Meals!", command=displayMeals)

# Layout commands
title.pack()
desc.pack()
foodBut.pack()
recipeBut.pack()
mealBut.pack()

root.mainloop()



