def displayInventory(dict):
    print("Inventory:")
    a = 0
    for k,v in dict.items():
        print(str(v) + " " +k)
        a += v
    print("Total number of items :" + str(a))
    
# 先把列表变成字典    再把键值对添加到字典
def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory.keys():
            inventory[addedItems[i]] += 1
        else:
            inventory.setdefault(addedItems[i],1)
    return inventory

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Inventory={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

Inventory = addToInventory(Inventory,dragonLoot)
displayInventory(Inventory)