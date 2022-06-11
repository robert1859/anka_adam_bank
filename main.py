
# def nazwa_funkcji(argumenty wejsciowe):
#     kod obslujacy funkcje
#     return wartosc/albo nic

def print_main_menu():
    print("Hi, this is best ATM in the world.")
    print("Tell me what do you want to do")
    print("1. Wplacic pieniadze")
    print("2. Wyplacic pieniadze")
    print("3. Sprawdzic stan konta")
    print("9. Menu Serwisanta")

def get_user_input():
    user_input = int(input("Podaj liczbe: "))
    return user_input

def check_user_input(user_input: int, expected_values: list) -> bool:
    if user_input in expected_values:
        return True
    return False

def authentication(user_input_pin, service_menu):
    if user_input_pin == 123456 or service_menu == 9:
        return True
    return False


# Main program loop
while True:
    user_input_pin = int(input("Enter PIN: "))
    print_main_menu()
    user_input = get_user_input()
    if not check_user_input(user_input, [1,2,3,9]):
        break
    if not authentication(user_input_pin, user_input):
        print("Invalid PIN")
        break
