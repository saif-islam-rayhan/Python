def all_exceptions_demo():
    try:
        # 1. ValueError: If input is not a number
        num = int(input("1. Enter a number: "))

        # 2. ZeroDivisionError: If number is 0
        result = 10 / num

        # 3. FileNotFoundError: If file does not exist
        with open("not_exist.txt", "r") as f:
            data = f.read()

        # 4. IndexError: If index is out of range
        my_list = [1, 2, 3]
        print("Item at index 3:", my_list[3])

        # 5. KeyError: If key not found in dictionary
        my_dict = {"name": "Rayhan"}
        print("Age:", my_dict["age"])

    except ValueError:
        print("ValueError: Input must be a number.")

    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero.")

    except FileNotFoundError:
        print("FileNotFoundError: The file does not exist.")

    except IndexError:
        print("IndexError: List index is out of range.")

    except KeyError:
        print("KeyError: Key not found in dictionary.")

    except Exception as e:
        print("Other Exception:", e)

    finally:
        print("Execution completed.")

all_exceptions_demo()
