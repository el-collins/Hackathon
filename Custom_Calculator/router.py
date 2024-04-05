from http.client import HTTPException
from typing import Annotated
from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/calculate/")
# Endpoint to perform arithmetic operations on two numbers
async def calculate(num1: float, num2: float, operation: str):
    """
    Calculates the result of an arithmetic operation between two numbers.

    :param num1: The first number.
    :param num2: The second number.
    :param operation: The arithmetic operation to perform. Can be 'add', 'subtract', 'multiply', 'divide', 'power', or 'sqrt'.
    :return: A dictionary containing the result of the operation.
    """
    # Check for valid operation
    if operation == "add" or operation == '+':
        result = num1 + num2
    elif operation == "subtract" or operation == '-':
        result = num1 - num2
    elif operation == "multiply" or operation == '*':
        result = num1 * num2
    elif operation == "divide" or operation == '/':
        # Check for division by zero
        if num2 == 0:
            return {"error": "Division by zero is not allowed"}
        result = num1 / num2
    elif operation == "power" or operation == '^':
        result = num1 ** num2
    elif operation == "sqrt":
        # Check for invalid input for square root calculation
        try:
            result = num1**0.5
        except ValueError:
            return {"error":"Invalid input for square root calculation"}
    else:
        return {"error": "Invalid operator"}
    
    return {"result": f"{num1} {operation} {num2} = {result}"}


@router.get("/convert/temperature")
# Endpoint to convert temperature from one unit to another
def convert_temperature(from_unit: Annotated[str, Query(..., choices=["Celsius", "Fahrenheit", "Kelvin"], description="")],
                        to_unit: Annotated[str, Query(..., choices=["Celsius", "Fahrenheit", "Kelvin"])],
                        value: Annotated[float, Query(...)]):
    """
    Converts temperature from one unit to another.

    :param from_unit: The unit of the input temperature. Can be 'Celsius', 'Fahrenheit', or 'Kelvin'.
    
    :param to_unit: The unit to convert the temperature to. Can be 'Celsius', 'Fahrenheit', or 'Kelvin'.
    
    :param value: The temperature value to convert. \n
    
    :return: The converted temperature value.
    """
    option = ["Celsius", "Fahrenheit", "Kelvin"]
    if from_unit not  in option or to_unit not in option:
        return {"error": "Invalid unit type. You can only convert Celcuius, Fahrenheit or Kelvin"}
    
    # Convert Fahrenheit to Celsius
    # Check if from_unit and to_unit are the same
    if from_unit == to_unit:
        return value
    
    # Perform temperature conversions
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        raise HTTPException(status_code=400, detail="Invalid temperature conversion")
    


@router.get("/factorial")
async def factorial(number:int):
    """Calculates the factorial of a number using recursion.\n
    If the number is negative it returns an error message.\n
    Otherwise, it will calculate and return the factorial of that number.\n
    
    :param number: An integer representing the number you want to find the factorial for.
    
    :return: The factorial of the inputted number.
    """
    if number < 0:
        return {"Error":"Number must be positive."}
    elif number == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, number+1):
            factorial *= i
        return factorial