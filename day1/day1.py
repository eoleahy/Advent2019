import math

fuel = lambda x: max(0, math.floor(x / 3) - 2)

def fuel_per_module(mass):

    module_fuel = 0
    while(mass > 0):
        module_fuel = fuel(mass) + module_fuel
        mass = fuel(mass)

    return module_fuel

def main():
    total_fuel = 0
    with open("input.txt","r") as f:

        lines = f.readlines()
        for module in lines:
            mass = float(module)
            total_fuel = total_fuel + fuel_per_module(mass)

    print("Total fuel: {}".format(total_fuel))


if __name__ == "__main__":
    main()