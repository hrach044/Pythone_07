import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory = dict()
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i].split(':')
        if len(arg) != 2:
            print(f"Error - invalid parameter '{arg[0]}'")
        else:
            try:
                if arg[0] in inventory:
                    print(f"Redundant item '{arg[0]}' - discarding")
                else:
                    inventory.update({arg[0]: int(arg[1])})
            except ValueError as e:
                print(f"Quantity error for '{arg[0]}': {e}")
        i += 1

    if len(inventory) == 0:
        print("No valid items provided. Usage: "
              "python3 ft_inventory_system.py <item>:<quantity> ...")
    else:
        print(f"Got inventory: {inventory}")
        print(f"Item list: {list(inventory.keys())}")
        print(f"Total quantity of the {len(inventory)} items: "
              f"{sum(inventory.values())}")

        for key, value in inventory.items():
            pr = round((value / sum(inventory.values()) * 100), 1)
            print(f"Item {key} represents {pr}%")

        max_q = None
        for value in inventory.values():
            if max_q is None or value > max_q:
                max_q = value
        for key, value in inventory.items():
            if max_q == value:
                print(f"Item most abundant: {key} with quantity {value}")
                break

        min_q = None
        for value in inventory.values():
            if min_q is None or value < min_q:
                min_q = value
        for key, value in inventory.items():
            if min_q == value:
                print(f"Item least abundant: {key} with quantity {value}")
                break

        inventory.update({'magic_item': 1})
        print(f"Updated inventory: {inventory}")
