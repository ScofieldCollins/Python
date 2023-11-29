def displayInventory(dict):
    print("Inventory:")
    a = 0
    for k,v in dict.items():
        print(str(v) + " " +k)
        a += v
    print("Total number of items :" + str(a))

Inventory={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(Inventory)