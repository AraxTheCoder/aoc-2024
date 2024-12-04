def a():
    with open("input.txt") as file:
        sum = 0
        for pot in file.read().split("mul("):
            po = pot.split(")")[0]

            potNumbers = po.split(",")
            
            if len(potNumbers) == 2:
                [first, second] = potNumbers

                try:
                    sum += int(first) * int(second)
                except: 
                    pass

        print(sum)

def b():
    with open("input.txt") as file:
        sum = 0
        enabled = True
        for pot in file.read().split("mul("):
            po = pot.split(")")[0]

            potNumbers = po.split(",")
            
            if len(potNumbers) == 2 and enabled:
                [first, second] = potNumbers

                try:
                    sum += int(first) * int(second)
                except: 
                    pass
            
            if "do()" in pot:
                enabled = True
            elif "don't()" in pot:
                enabled = False

        print(sum)


a()
b()