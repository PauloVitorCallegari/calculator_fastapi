from pydantic import BaseModel

class CalculatorInput(BaseModel):
    value1: float
    value2: float