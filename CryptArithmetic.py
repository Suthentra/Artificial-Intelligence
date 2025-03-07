from itertools import permutations

def solve_cryptarithmetic(equation1, equation2, result):
    letters = set(equation1 + equation2 + result)
    if len(letters) > 10:
        print("Too many unique letters to map to digits.")
        return

    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if mapping[equation1[0]] == 0 or mapping[equation2[0]] == 0 or mapping[result[0]] == 0:
            continue  # Skip if a number starts with zero
        
        num1 = int("".join(str(mapping[ch]) for ch in equation1))
        num2 = int("".join(str(mapping[ch]) for ch in equation2))
        num_result = int("".join(str(mapping[ch]) for ch in result))
        
        if num1 + num2 == num_result:
            print(f"Solution for {equation1} + {equation2} = {result}:")
            print(f"  {num1}")
            print(f"+ {num2}")
            print("------")
            print(f" {num_result}")
            print("Values:")
            for key, value in sorted(mapping.items()):
                print(f"{key} = {value}")
            break

# Solve the given problems
print("Solving SEND + MORE = MONEY")
solve_cryptarithmetic("SEND", "MORE", "MONEY")

print("\nSolving BASE + BALL = GAMES")
solve_cryptarithmetic("BASE", "BALL", "GAMES")
