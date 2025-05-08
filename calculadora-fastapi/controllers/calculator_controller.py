def add(value1: float, value2: float) -> float:
    return value1 + value2

def subtract(value1: float, value2: float) -> float:
    return value1 - value2

def multiply(value1: float, value2: float) -> float:
    return value1 * value2

def divide(value1: float, value2: float) -> float:
    if value2 == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return value1 / value2