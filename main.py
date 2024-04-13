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

# Ejemplo de uso
numbers = [24, 36, 48, 60]
mcd_calculator = MCDCalculator(numbers)
mcd = mcd_calculator.find_mcd()
print(f"El MCD de {numbers} es: {mcd}")
