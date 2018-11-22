def calc_hypo(a, b)
    if type(a) not in (int, float) or type(b) not in (int, float)
        print("bad argument")
        return False
    if a <= 0 or b <= 0
        print("bad argument")
        return False
    hypo = (a**2 + b**2)**(1/2)]
    return hypo
