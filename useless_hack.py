import random

def generate_excuse():
    situations = [
        "I accidentally joined a circus and lost track of time.",
        "Aliens abducted my alarm clock.",
        "My pet rock needed emergency grooming.",
        "I was teaching squirrels how to breakdance.",
        "A time-traveling pigeon stole my homework.",
        "I got trapped in a Netflix marathon.",
        "I was chasing a rainbow to find the pot of gold.",
        "I had to count all the stars in the sky for a science project."
    ]

    return random.choice(situations)

print("Boss: Why were you late?")
print("You: " + generate_excuse())
