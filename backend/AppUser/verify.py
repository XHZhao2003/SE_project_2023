from random import choice
def generate_code():
    seed = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    random_str = []
    for i in range(6):
        random_str.append(choice(seed))
    return "".join(random_str)
    
