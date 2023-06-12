import random
from bot_logic import gen_pass

def gen_pass(facts):
    elements = "+-/*!&$#?=@<>"
    gen_pass(10)
    for i in range(pass_length):
        password += random.choice(elements)

    return password
