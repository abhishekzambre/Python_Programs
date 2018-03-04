def findRestaurant(list1, list2):
    Aindex = {u: i for i, u in enumerate(list1)}

    print(Aindex)
    out = []
    for l1 in list1:
        for l2 in list2:
            if l1 == l2:
                 out.append(l1)
    return out

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Burger King", "Tapioca Express", "Shogun"]

print(findRestaurant(list1, list2))
