import math
import random

class Brand:
    def __init__(self, name, length, first_digits):
        self.name = name
        self.length = length
        self.first_digits = first_digits

class CreditNumber:
    def __init__(self, brand="", number=""):
        self.brand = brand
        self.number = [int(digit) for digit in number]

    def findBrand(self, brands):
        first_digits = self.number[0] * 10 + self.number[1]
        for brand in brands:
            if len(self.number) in brand.length and str(first_digits) in brand.first_digits:
                self.brand = brand.name
                return brand.name
        else:
            return "Invalid"

    def generate(self):
        self.number = []
        first_digits = random.choice(self.brand.first_digits)
        for digit in first_digits:
            self.number.append(int(digit))
        length = random.choice(self.brand.length)
        for _ in range(length - len(self.number)):
            self.number.append(random.randint(0, 9))

    def luhnAlg(self):
        luhn_sum = 0
        for i in reversed(range(len(self.number))):
            if i % 2 + len(self.number) % 2 != 1:
                digit = self.number[i] * 2
                luhn_sum += math.floor(digit / 10) + digit % 10
            else:
                luhn_sum += self.number[i]
        return luhn_sum

    def fix(self, luhn_sum):
        minus = luhn_sum % 10
        for i in reversed(range(len(self.number))):
            if minus <= 0:
                return
            elif i % 2 + len(self.number) % 2 == 1:
                if self.number[i] - minus >= 0:
                    self.number[i] -= minus
                    return
                else:
                    minus = minus - self.number[i]
                    self.number[i] = 0

    def string(self):
        return "".join([str(number) for number in self.number])

def generate(brand):
    credit = CreditNumber(brand=brand)
    credit.generate()
    luhn_sum = credit.luhnAlg()
    credit.fix(luhn_sum)
    return credit.string()

def validate(number, brands):
    credit = CreditNumber(number=number)
    luhn_sum = credit.luhnAlg()
    if luhn_sum % 10 == 0:
        brand = credit.findBrand(brands)
        return f"Valid, Brand: {brand}"
    else:
        return "Invalid"