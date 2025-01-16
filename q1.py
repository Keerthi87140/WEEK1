def fullname(first_name, last_name):
    return f"{first_name} {last_name}"

def string_alternative(input_string):
    return input_string[::2]

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    full_name = fullname(first_name, last_name)
    
    result = string_alternative(full_name)
    
    print(f"Full name: {full_name}")
    print(f"String with alternative characters: {result}")

if __name__ == "__main__":
    main()