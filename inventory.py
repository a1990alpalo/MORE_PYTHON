products = [
    {"name": "Tennis Racket", "price": 120, "stock": 5},
    {"name": "Football", "price": 30, "stock": 12},
    {"name": "Smart Watch", "price": 250, "stock": 3},
    {"name": "Running Shoes", "price": 95, "stock": 8}
]


def display_inventory(products):
    print("=== SPORTS STORE INVENTORY ===\n")

    for index, product in enumerate(products, start=1):
        print(f"{index}. {product['name']}")
        print(f"   Price: ${product['price']}")
        print(f"   Stock: {product['stock']}")

        if product["stock"] < 5:
            print("   ⚠️ Low Stock!")

        print()


def calculate_total_value(products):
    total_value = 0

    for product in products:
        inventory_value = product["price"] * product["stock"]
        total_value += inventory_value

    return total_value


def display_total_value(products):
    total_value = calculate_total_value(products)
    print(f"Total Inventory Value: ${total_value}")


def main():
    display_inventory(products)
    display_total_value(products)


if __name__ == "__main__":
    main()