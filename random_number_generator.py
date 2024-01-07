class RandomGenerator:
    def __init__(self, seed):
        self.seed = seed
    
    def generate_random_number(self):
        # Linear Congruential Generator (LCG)
        # These values are chosen somewhat arbitrarily for demonstration purposes
        a = 1103515245
        c = 12345
        m = 2 ** 31

        self.seed = (a * self.seed + c) % m
        return self.seed

# Example usage:
seed_value = 42  # Initial seed value
random_generator = RandomGenerator(seed_value)

for i in range(1):
    random_number = random_generator.generate_random_number()
    print("Random number:", random_number)
