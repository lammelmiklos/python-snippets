    """Using a List and Adding Boolean values in the Index field
    lets us create a switch-case kind of functioning
    where we have ranges of values
    """

def bmi(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]