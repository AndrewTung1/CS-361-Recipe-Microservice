import json
import time

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
DATA_FILE = "recipe_data.json"


def read_input():
    with open(INPUT_FILE, 'r') as input_file:
        return [line.strip() for line in input_file if line.strip()]

def load_data():
    try:
        with open(DATA_FILE, 'r') as json_data:
            return json.load(json_data)
    # If there is currently no data, we set the data to be an empty list
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        return []

def save_data(data):
    with open(DATA_FILE, 'w') as json_data:
        json.dump(data, json_data, indent=4)

def add(lines, data):
    if len(lines) < 4:
        return
    recipe = {
        "recipe_name": lines[1],
        "ingredients": lines[2],
        "instructions": lines[3]
    }
    data.append(recipe)
    save_data(data)

def names(data):
    with open(OUTPUT_FILE, 'w') as output:
        for recipe in data:
            output.write(recipe["recipe_name"] + '\n')

def details(lines, data):
    if len(lines) < 2:
        return
    name = lines[1]
    found = False
    with open(OUTPUT_FILE, 'w') as output:
        for recipe in data:
            if recipe["recipe_name"] == name:
                output.write(recipe["recipe_name"] + '\n')
                output.write(recipe["ingredients"] + '\n')
                output.write(recipe["instructions"] + '\n')
                found = True
                break
        if not found:
            output.write("Recipe Not Found\n")

def process_instruction():
    lines = read_input()
    if not lines:
        return
    data = load_data()
    command = lines[0]
    if command == "Add":
        add(lines, data)
    elif command == "Names":
        names(data)
    elif command == "Details":
        details(lines, data)
    open(INPUT_FILE, 'w').close()


while True:
    process_instruction()
    time.sleep(1)
