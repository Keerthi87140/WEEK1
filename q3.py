def inches_to_cm(heights):
    return [round(height * 2.54, 2) for height in heights]

def cm_to_inches(heights):
    return [round(height / 2.54, 2) for height in heights]

def main():
    print("Choose the conversion type:")
    print("1: Inches to Centimeters")
    print("2: Centimeters to Inches")
    choice = input("Enter 1 or 2: ").strip()
    
    if choice not in ['1', '2']:
        print("Invalid choice. Please restart the program.")
        return
    
    input_heights = input("Enter heights separated by commas: ")
    try:
        heights = [float(height.strip()) for height in input_heights.split(",")]
    except ValueError:
        print("Invalid input. Please enter numeric values separated by commas.")
        return
    
    if choice == '1':
        converted_heights = inches_to_cm(heights)
        print("Converted heights (in cm):", converted_heights)
    elif choice == '2':
        converted_heights = cm_to_inches(heights)
        print("Converted heights (in inches):", converted_heights)

if __name__ == "__main__":
    main()