import functions

while True:
    try:
        weight = float(input("Inform your Weight in Kilograms so i can calculate your BMI! "))
        height = float(input("Inform your Height in Meters so i can calculate your BMI! "))
        
        result = functions.operation(weight, height)    
        
        if result is None:
            print("Weight and Height must be greater than Zero! Please try again!")
            continue

        print(f"Your BMI is {result:.2f}")

        if not functions.question():
            break

    except ValueError:
        print("Those are invalid values! Please try again!")

