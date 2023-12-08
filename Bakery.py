print("Welcome to the barekat bakery")

nan_dict = {'Lavash': 1000, 'Barbary': 2000, 'Sangak': 4000, 'Tafton': 2000, 'Baget': 6000}

print("we have five of bread:\n")
for nan, gheymat in nan_dict.items():
    print(f'{nan} - {gheymat} Toman')

while True:
    nan = input("\n What kind of bread do you want?")
    if nan in nan_dict:
        break
    else:
        print("Sorry, we do not have this bread.  Please try again.")

while True:
    try:
        tedad = int(input(f"How many {nan} do you want?"))
        break
    except ValueError:
        print("Please enter a valid number")

total_price = nan_dict[nan] * tedad

while True:
    response = input("\nDo you want to order bread again? (yes/no) ").lower()
    if response == 'yes':
        while True:
            nan = input("\n What kind of bread do you want?")
            if nan in nan_dict:
                break
            else:
                print("Sorry, we do not have this bread.  Please try again.")
        while True:
            try:
                tedad = int(input(f"How many {nan} do you want?"))
                break
            except ValueError:
                print("Please enter a valid number")
        total_price += nan_dict[nan] * tedad
    elif response == 'no':
        break
    else:
        print("Please enter a yes or no answer")

print(f"\nThank you for your purchase. The total price of your order is : {total_price} Toman ")

print("Thank you for your purchase")