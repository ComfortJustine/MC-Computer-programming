class Calculator:
    """
    A simple calculator class that provides basic arithmetic operations.    
    """

    def_ _int_ _(self):

    """
        initializes a new Calculator object.
    """

    pass

    def add(self, a, b):
        """
        Adds two numbers.

        Args:
           a (float): The first number.
           b (float): The second number.

        Returns:
            float: The result of the addition operation.
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtracts one number from another.


        Args:
            a (float): The numberfrom which subtraction is done.
            b (float): The number to subtract.

        Returns:
             float: The result of the subtraction operation.
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiplies two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The result of the multiplication operation.
        """
        return a * b

    def divide(self, a, b):
        """
        Divides one number by another.

        Args:
            a (float): The numerator.
            b(float): The denominator.

        Returns:
            float: The result of the division operation.
        """

        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b        

