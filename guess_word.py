import random as rd

import random
#define word library and corresponding hint of the word
word_bank = {
    "Fruits": [
        ("apple", "Keeps the doctor away"),
        ("banana", "Long yellow fruit"),
        ("mango", "King of fruits"),
        ("orange", "A citrus fruit")
    ],

    "Animals": [
        ("tiger", "National animal of Nepal"),
        ("elephant", "Largest land animal"),
        ("rabbit", "Likes carrots"),
        ("dog", "Known as man's best friend")
    ],

    "Technology": [
        ("python", "A popular programming language"),
        ("keyboard", "Used to type"),
        ("computer", "Electronic machine"),
        ("internet", "Connects the world")
    ],

    "Places": [
        ("nepal", "Home of Mount Everest"),
        ("kathmandu", "Capital city of Nepal"),
        ("paris", "City of love"),
        ("london", "Capital of the UK")
    ]
}
#display the menu

print("--------------------Guess The Word-----------------------")
print("you can choose words from your choice if category.")
print("categories:\n1.Animal\n2.fruits\n3.places\n4.technology")
user_category=input(print("enter choice of category"))
word,hint=random.choice(word_bank[user_category])

print("lets start!!!\n")

guessedword="_"*len(word)
print(hint)
inp_letter=input("enter guess letter:")
if inp_letter in 
