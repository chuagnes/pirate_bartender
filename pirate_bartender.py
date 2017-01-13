import random

def what_drink():
    questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
    }

    answers = {
    "strong":"",
    "salty":"",
    "bitter":"",
    "sweet":"",
    "fruity":"",
    }
    
    customers = {}
    name = input("What is your name? ")
    
    if name in customers:
        return customers[name] #not sure why this isn't working...
        print(customers)
    else:
        for c in questions:
            n = input(questions[c] + ' Enter Y/N. ')
            if n.lower() == 'y' or n.lower() == 'yes':
                answers[c] = True
            else:
                answers[c] = False
        customers[name] = answers
        return answers
    
    
def mix_drink(answers):
    ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
    }
    
    drink = []
    
    for c in answers:
        if answers[c] == True:
            drink.append(random.choice(ingredients[c]))
    
    return drink

def drink_name():
    adjectives = ["noble","fiery","insane","numbing","Wondrous"]
    nouns = ["witch brew","Sailor Flask","hug","hair of dog","liquid courage"]
    drinkname = random.choice(adjectives)+" "+random.choice(nouns)
    return drinkname

if __name__ == '__main__':
    print("Your drink is {}, which contains {}".format(drink_name(), mix_drink(what_drink())))
    n = input("Would you like another drink? Enter Y/N. ")
    
    while n.lower() == 'y' or n.lower() == 'yes':
        print(mix_drink(what_drink()))
        n = input("Would you like another drink? Enter Y/N. ")
    else:
        print("Hope you enjoyed your drink!")
        
        
        
    