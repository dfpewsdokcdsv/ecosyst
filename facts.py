import random
from bot_logic import gen_pass

def gen_pass(facts):
    elements = "1. Найди людное место и попробуй поискать мусора. Не забудь взять пакет! 2. Попробуй пойти вместе со своими друзьями.",
                  "Вместе интересней.",
                  "3. Если вы найдете какие-нибудь батарейки, несите их на переработку."
    facts = ""
    gen_pass(10)
    for i in range(facts):
        facts += random.choice(elements)

    return facts
