mult_count = 0
add_count = 0

def evalpoly(coefs: list, x: float) -> float:
    global mult_count
    global add_count
    
    expr = 0
    xPow = x**(len(coefs) - 1)
    for i in range(len(coefs) - 1, -1, -1):
        mult_count += 1
        add_count += 1
        expr += coefs[i] * xPow
        xPow /= x
        mult_count += 1

    return expr


def evalpolybetter(coefs:list, x:float) -> float:
    global mult_count
    global add_count

    expr = 0
    xPow = 1
    for i in range(0, len(coefs)):
        mult_count += 1
        add_count += 1
        expr += coefs[i] * xPow
        xPow *= x
        mult_count += 1


if __name__ == "__main__":
    coefs = [1, 2, 6, 3, 7, 0, 5, 4]
    x = 1
    print(f"p({x}) = ", evalpoly(coefs, x), sep="")
    print(f"mults = {mult_count}\tadds = {add_count}")

    mult_count = 0
    add_count = 0
    print(f"p({x}) = ", evalpolybetter(coefs[::-1], x), sep="")
    print(f"mults = {mult_count}\tadds = {add_count}")