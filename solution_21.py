
class Recipe:
    def __init__(self, line):
        ing, aler = line.split(" (")
        self.ingredients = ing.split(" ")
        self.alergens = aler[9:-1].split(", ")

    def delete_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)

    def delete_alergen(self, alergen):
        if alergen in self.alergens:
            self.alergens.remove(alergen)


if __name__ == "__main__":

    file_name = "test_21.txt"
    file_name = "input_21.txt"
    recipes = [Recipe(line.strip()) for line in open(file_name)]

    alergens = [alergen for recipe in recipes for alergen in recipe.alergens]
    ingredients = [
        ingredient for recipe in recipes for ingredient in recipe.ingredients]
    alergens = list(set(alergens))
    orig_alergens = alergens.copy()
    ingredients = list(set(ingredients))

    alergic_ingredients = {}

    while len(alergens) != 0:
        to_delete = []
        for alergen in alergens:
            potentials = ingredients.copy()
            for recipe in recipes:
                if alergen in recipe.alergens:
                    potentials = (
                        list(set(potentials) & set(recipe.ingredients)))
            if len(potentials) == 1:
                alergic_ingredients[alergen] = potentials[0]
                for recipe in recipes:
                    recipe.delete_ingredient(potentials[0])
                    recipe.delete_alergen(alergen)
                to_delete.append(alergen)
        for td in to_delete:
            alergens.remove(td)

    leftovers = {}
    for recipe in recipes:
        for ing in recipe.ingredients:
            if ing in leftovers:
                leftovers[ing] += 1
            else:
                leftovers[ing] = 1

    print("part 1: ", sum([n for _, n in leftovers.items()]))

    s = []
    for alergen in sorted(orig_alergens):
        if alergen in alergic_ingredients:
            s.append(alergic_ingredients[alergen])
    # dhfng,pgblcd,xhkdc,ghlzj,dstct,nqbnmzx,ntggc,znrzgs
    print("part 2: ", ",".join(s))
