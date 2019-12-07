class Number:
    def __init__(self, value):
        print("Metoda init wywołana")
        self.value = value
    def wyzeruj(self):
        self.value = 0
    def ustaw(self, ustaw):
        self.value = ustaw

numer = Number(2)
numer.wyzeruj()
print(numer.value)
numer.ustaw(9)
print(numer.value)
