import pyfiglet
import random

font = random.choice(pyfiglet.FigletFont.getFonts())
art = pyfiglet.figlet_format("Eid-ul-Adha", font=font)
greeting = f"{art}\n Eid ul Adha Mubarak!\n{art}"
print(greeting)

