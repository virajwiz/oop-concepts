class Calculate():
    def divide(self, x, y):
        try:
            return x/y
        except ZeroDivisionError as e:
            print("Cannot divide by zero")
            return 0
        except TypeError as e:
            print("Typeerror: invalid input")
            return 0
        except Exception as e:
            print(f"an exception of type {type(e).__name__} occured:{e}")
            return 0
        finally:
            print("Execution complete")