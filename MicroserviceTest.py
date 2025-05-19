import time

def add_recipe(recipe_name, ingredients, instructions):
    with open("input.txt", "w") as file:
        file.write("Add\n" )
        file.write(recipe_name + '\n')
        file.write(ingredients + '\n')
        file.write(instructions + '\n')
    time.sleep(2)

def write_names():
    with open("input.txt", "w") as file:
        file.write("Names\n")
    time.sleep(3)
    with open("output.txt", 'r') as output:
        lines = [line.strip() for line in output if line.strip()]
    for name in lines:
        print(name + '\n')
    time.sleep(2)

def get_recipe_details(recipe_name):
    with open("input.txt", "w") as file:
        file.write("Details\n")
        file.write(recipe_name + '\n')
    time.sleep(2)
    with open("output.txt", 'r') as output:
        lines = [line.strip() for line in output if line.strip()]
    for detail in lines:
        print(detail + '\n')
    time.sleep(1)


add_recipe("Rice", "Rice, Water", "Wash rice and then put in rice cooker and hit cook")
add_recipe("Pizza", "Dough, Tomato Sauce, Cheese", "Roll dough, pour sauce, place cheese, put in oven")
write_names()
print("----------------------------------------------------------------------------------")
get_recipe_details("Rice")
print("----------------------------------------------------------------------------------")
get_recipe_details("Pizza")
print("----------------------------------------------------------------------------------")







