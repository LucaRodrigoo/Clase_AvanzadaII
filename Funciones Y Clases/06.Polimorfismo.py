import os
os.system('cls' if os.name == 'nt' else 'clear')

class perro:
    def hablar(self):
        print("Guau")
class gato:
    def hablar(Self):
        print("Miau")

hachiko=perro()
garfield=gato()
for animal in [hachiko,garfield]:
    animal.hablar()