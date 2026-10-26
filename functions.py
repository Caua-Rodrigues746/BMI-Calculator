def operation(weight, height):
    if weight <= 0:
        return None

    if height <= 0:
        return None
    
    math = weight / (height ** 2)
    return math

def question():
    while True:
        question = input("Do you want to perform another calculation? Type Yes or No! ").lower()

        if question == "yes":
            print("Let's do it again!")
            return True

        elif question == "no":
            return False

        else:
            print("It must be Yes or No! Please try again! ")