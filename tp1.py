

import math 

def faire_la_vaisselle(sale_vaisselle: bool, lave_vaisselle: bool) -> bool:
    return not lave_vaisselle and sale_vaisselle
print(faire_la_vaisselle(True, True)) 





# ex4

def test_nombre(number: int) -> bool:
    """
    Args:
        number (int): _description_

    Returns:
        bool: _description_
    """
    return number % 3 == 0 and number < 100
print(test_nombre(120))


# exercice6
def airetiangle(a: int, b: int, c: int) -> float:
    p: float = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))
    

def volumetetraedre(a: float, b: float, c: float, d: float, e: float, f: float) -> float:
    """_summary_

    Args:
        a (float): cote a
        b (float): cote b
        c (float): cote c
        d (float): cote d
        e (float): cote e
        f (float): cote f

    Returns:
        float: the volume 
    """
    x: float = a**2+b**2-d**2
    y: float = b**2+c**2-e**2
    z: float = a**2+c**2-f**2
    
    p: float = 4*((a**2)*(b**2)*(c**2))
    q: float = (a**2*x**2) + (b**2*z**2) + (c**2*y**2)
    r: float = x*y*z
    return (1/12)*(math.sqrt(p-q+r))

print(volumetetraedre(1, 1, 1, 1, 1, 1))


def volumetetraedreregulier(l: float) -> float:
    """
    Args:
        l (float): longeur 
    Returns:
        float: volume of tetraed
    """
    return (math.sqrt(2)/12)*(l**3)

