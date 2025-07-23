def analyze_purchase():
    try:
        filename = input("Enter the file name: ") + ".txt"
        with open(filename, 'r') as file:
            lines = file.readlines()

        items_purchased = 0
        free_items = 0
        total_amount = 0
        discount = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue  
            parts = line.split()

            if len(parts) == 2:
                item, price = parts[0], parts[1]

                if item.lower() == "discount":
                    try:
                        discount = int(price)
                    except ValueError:
                        print("Invalid discount format.")
                elif price.lower() == "free":
                    free_items += 1
                else:
                    try:
                        price_value = int(price)
                        total_amount += price_value
                        items_purchased += 1
                    except ValueError:
                        print(f"Invalid price format for item: {item}")
            else:
                print(f"Malformed line: {line}")

        final_amount = total_amount - discount

        print("No of items purchased:", items_purchased)
        print("No of free items:", free_items)
        print("Amount to pay:", total_amount)
        print("Discount given:", discount)
        print("Final amount paid:", final_amount)

    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
    except Exception as e:
        print("An unexpected error occurred:", e)


analyze_purchase()
