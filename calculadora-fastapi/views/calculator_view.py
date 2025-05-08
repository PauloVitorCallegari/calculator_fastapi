from fastapi import APIRouter, HTTPException
from models.calculator_model import CalculatorInput
from controllers import calculator_controller as controller

router = APIRouter(prefix="/calculator", tags=["Calculator"])

@router.post("/add")
def add(input: CalculatorInput):
    result = controller.add(input.value1, input.value2)
    return {"operation": "addition", "result": result}

@router.post("/subtract")
def subtract(input: CalculatorInput):
    result = controller.subtract(input.value1, input.value2)
    return {"operation": "subtraction", "result": result}

@router.post("/multiply")
def multiply(input: CalculatorInput):
    result = controller.multiply(input.value1, input.value2)
    return {"operation": "multiplication", "result": result}

@router.post("/divide")
def divide(input: CalculatorInput):
    try:
        result = controller.divide(input.value1, input.value2)
        return {"operation": "division", "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))