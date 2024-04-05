# Custom Calculator API

## Overview
The Custom Calculator API is a versatile FastAPI application designed to perform a variety of arithmetic operations, conversions, and basic logical operations. This project serves as a practical test of a student's ability to implement logical functions in endpoints, manage different parameter types, and return calculated results based on user input.

## Features and Routes

### Arithmetic Operations: `/calculate`
- **POST Request Body**: Accepts an `operation` (add, subtract, multiply, divide) and two `operands`.
- **Response**: The result of the arithmetic operation.
- **Validations**: Includes checks for division by zero.

### Convert Temperature: `/convert/temperature`
- **GET Query Parameters**: 
  - `from`: The original temperature unit (Celsius, Fahrenheit, Kelvin).
  - `to`: The target temperature unit.
  - `value`: The temperature value to convert.
- **Response**: The converted temperature value.
- **Logic**: Converts between Celsius, Fahrenheit, and Kelvin.

### Factorial Calculator: `/factorial`
- **GET Query Parameter**: 
  - `n`: An integer for which the factorial is to be calculated (max 20).
- **Response**: The factorial of `n`.
- **Validations**: Ensures `n` is a non-negative integer and within limits to prevent long processing times.

### Simple Interest Calculator: `/interest`
- **GET Query Parameters**: 
  - `principal`: The principal amount.
  - `rate`: The rate of interest.
  - `time`: The time period in years.
- **Response**: The calculated simple interest.
- **Validations**: Handles multiple query parameters with appropriate validations.

### Palindrome Checker: `/palindrome`
- **GET Query Parameter**: 
  - `text`: The string to check for palindrome property.
- **Response**: A boolean indicating whether the `text` is a palindrome or not.

## Getting Started
To use the Custom Calculator API, clone the repository and install the required dependencies. Ensure you have FastAPI and Uvicorn installed to run the application.

```bash
git clone https://github.com/your-repository/custom-calculator-api.git
cd custom-calculator-api
pip install -r requirements.txt
uvicorn main:app --reload
```

## Documentation
Once the server is running, navigate to `http://127.0.0.1:8000/docs` to view the Swagger UI documentation that provides interactive exploration of the API's capabilities.

## Testing
Comprehensive test cases are provided to validate the functionality of each endpoint. Run the test suite to ensure all operations are performing as expected.

```bash
pytest
```

## Contribution
Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.

---

This README provides a concise overview of the Custom Calculator API project. For detailed instructions and more information, please refer to the full documentation in the repository. Happy calculating! 🧮🚀