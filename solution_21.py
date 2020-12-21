import numpy as np
import itertools


class Recipe:
    def __init__(self, line):
        if "contains" not in line:
            print("assumption wrong")
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

    alergens = []
    ingredients = []
    for recipe in recipes:
        alergens.extend(recipe.alergens)
        ingredients.extend(recipe.ingredients)
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

    m = 0
    for _, n in leftovers.items():
        m += n
    print("part 1: ", m)  # 2436

    s = ""
    for alergen in sorted(orig_alergens):
        print(alergen)
        if alergen in alergic_ingredients:
            s = s+alergic_ingredients[alergen]+","
    print(s[:-1]) #dhfng,pgblcd,xhkdc,ghlzj,dstct,nqbnmzx,ntggc,znrzgs
