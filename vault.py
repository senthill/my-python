class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.kunts = knuts
    
    def __str__(self):
        return f"Vault: {self.galleons} galleons, {self.sickles} sickles, {self.kunts} kunts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        kunts = self.kunts + other.kunts
        return Vault(galleons, sickles, kunts)

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(50, 25, 10)
print(weasley)

# galleons = potter.galleons + weasley.galleons
# sickles = potter.sickles + weasley.sickles
# kunts = potter.kunts + weasley.kunts

# total = Vault(galleons, sickles, kunts)
# print(total)

total = potter + weasley
print(total)