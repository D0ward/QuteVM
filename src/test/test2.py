import string
from math import log10

class Task2:
    # If you aren't so lasy as me, you can make it manually (bitwise addition)
    '''
    Converting a number from the numeral base n to m while maintaining accuracy
    '''
    def __init__(self):
        self.integer = 0
        self.fractio = 0.0
        self.res = ""
        self.old_base = 10
        self.new_base = 10
        self.accuracy = 10
        self.dict = string.ascii_uppercase

    def __solve_accuracy(self):
        self.accuracy = int((len(str(self.fractio)) * log10(self.old_base)) // log10(self.new_base)) + 1

    def __to_decimal_integer(self):
        self.integer = int(self.integer, self.old_base)

    def __to_decimal_fractional(self):
        decimal_value = 0.0
        for i, char in enumerate(self.fractio, 1):
            try:
                digit = int(char, self.old_base)
            except ValueError:
                raise ValueError(f"Недопустимый символ '{char}' для системы с основанием {self.old_base}")
        
            decimal_value += digit * (self.old_base ** -i)
    
        self.fractio = decimal_value
        

    def __from_decimal_integer(self):
        while self.integer >= self.new_base:
            self.res += str(self.integer % self.new_base)
            self.integer //= self.new_base
        self.res += str(self.integer % self.new_base)
        self.res = self.res[::-1]

    def __from_decimal_fractio(self):

        for _ in range(self.accuracy):
            self.fractio *= self.new_base
            self.res += str(int(self.fractio))
            self.fractio -= int(self.fractio)

    def process(self, number: str = "155.006", systems: tuple = (8, 9)) -> str:
        """
        :param number
        :param system: system of operands
        :return: converted number
        """
        self.integer, self.fractio = number.split(".")
        self.old_base, self.new_base = systems
        self.__solve_accuracy()

        self.__to_decimal_integer()
        self.__to_decimal_fractional()

        self.__from_decimal_integer()
        self.res += '.'
        self.__from_decimal_fractio()
        return self.res


if __name__ == "__main__":
    task2 = Task2()
    print(task2.process())
