import sys

def solve():
    try:
        # The code is designed to read from standard input,
        # which is the most common way to handle competitive
        # programming problems.
        n = int(sys.stdin.readline())
        recipes = {}
        for _ in range(n):
            line = sys.stdin.readline().strip()
            if not line:
                continue
            
            result, ingredients_str = line.split('=')
            ingredients = ingredients_str.split('+')
            
            if result not in recipes:
                recipes[result] = []
            recipes[result].append(ingredients)
        
        target_potion = sys.stdin.readline().strip()
    except (IOError, ValueError) as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        return

    memo = {}

    def get_min_orbs(potion_name):
        if potion_name in memo:
            return memo[potion_name]
        
        if potion_name not in recipes:
            # It's an item, not a potion
            return 0
        
        min_cost = float('inf')
        
        # We need to consider all possible recipes for this potion
        for ingredient_list in recipes[potion_name]:
            # The base cost for any recipe is the number of ingredients minus 1
            current_cost = len(ingredient_list) - 1
            
            # Now, add the cost of brewing each ingredient
            for ingredient in ingredient_list:
                # If the ingredient is a potion, recursively find its minimum cost
                if ingredient in recipes:
                    current_cost += get_min_orbs(ingredient)
            
            # Find the minimum cost among all recipes for the current potion
            min_cost = min(min_cost, current_cost)
            
        memo[potion_name] = min_cost
        return min_cost

    result = get_min_orbs(target_potion)
    print(result)

if __name__ == "__main__":
    solve()
