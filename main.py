class MCDCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_mcd(self):
        # Encuentra el MCD de una lista de números utilizando el algoritmo de Euclides
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if len(self.numbers) < 2:
            return None

        result = self.numbers[0]
        for num in self.numbers[1:]:
            result = gcd(result, num)
        return result

    def find_mcm(self):
        # Encuentra el MCM de una lista de números utilizando la relación entre MCD y MCM
        def lcm(a, b):
            return a * b // gcd(a, b)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if len(self.numbers) < 2:
            return None

        result = self.numbers[0]
        for num in self.numbers[1:]:
            result = lcm(result, num)
        return result

# Ejemplo de uso
numbers = [24, 36, 48, 60]
mcd_calculator = MCDCalculator(numbers)
mcd = mcd_calculator.find_mcd()
mcm = mcd_calculator.find_mcm()
print(f"El MCD de {numbers} es: {mcd}")
print(f"El MCM de {numbers} es: {mcm}")
