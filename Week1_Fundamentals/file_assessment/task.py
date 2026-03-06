import json

new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}

# Task 1 — Read inventory file
with open("Week1_Fundamentals/file_assessment/inventory.json", "r") as file:
    inventory = json.load(file)

print("Total number of books:", len(inventory))


# Task 2 — Append new book and save
inventory.append(new_book)

with open("Week1_Fundamentals/file_assessment/inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)


# Task 3 — Read again and display inventory
with open("Week1_Fundamentals/file_assessment/inventory.json", "r") as file:
    updated_inventory = json.load(file)

for book in updated_inventory:
    print("Title:", book["title"], "| Author:", book["author"], "| Price: $"+str(book["price"]))