
class Recipe:
    def __init__(self, line):
        ing, aler = line.split(" (")
        self.ingredients = ing.split(" ")
        self.alergens = aler[9:-1].split(", ")


if __name__ == "__main__":

    file_name = "test_21.txt"
    file_name = "input_21.txt"
    recipes = [Recipe(line.strip()) for line in open(file_name)]

    alergens = list(
        set([alergen for recipe in recipes for alergen in recipe.alergens]))
    ingredients = list(set([
        ingredient for recipe in recipes for ingredient in recipe.ingredients]))

    alergic_ingredients = {}
    while len(alergic_ingredients) != len(alergens):
        for alergen in alergens:
            potentials = ingredients.copy()
            for recipe in recipes:
                if alergen in recipe.alergens:
                    potentials = (
                        list(set(potentials) & set(recipe.ingredients)))
            if len(potentials) == 1:
                alergic_ingredients[alergen] = potentials[0]
                for recipe in recipes:
                    if potentials[0] in recipe.ingredients:
                        recipe.ingredients.remove(potentials[0])
                    if alergen in recipe.alergens:
                        recipe.alergens.remove(alergen)

    leftovers = {}
    for recipe in recipes:
        for ing in recipe.ingredients:
            if ing in leftovers:
                leftovers[ing] += 1
            else:
                leftovers[ing] = 1
    print("part 1: ", sum([n for _, n in leftovers.items()]))

    s = []
    for alergen in sorted(alergens):
        if alergen in alergic_ingredients:
            s.append(alergic_ingredients[alergen])
    # dhfng,pgblcd,xhkdc,ghlzj,dstct,nqbnmzx,ntggc,znrzgs
    print("part 2: ", ",".join(s))
