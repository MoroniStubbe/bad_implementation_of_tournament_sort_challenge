import random
import copy

def is_sorted(l):
    return all(l[i] <= l[i+1] for i in range(len(l) - 1))

def get_winners(l_enum):
    l_enum = copy.copy(l_enum)
    winners = []
    l_enum_len = len(l_enum)
    l_enum_len_is_odd = l_enum_len & 1
    if l_enum_len_is_odd:
        winners.append(l_enum[l_enum_len - 1])

    i = 1
    while i < l_enum_len:
        i2 = i - 1
        item1 = l_enum[i][1]
        item1_compared_item_indexes = [compared_item[0] for compared_item in item1[2]]
        item2 = l_enum[i2][1]
        item2_compared_item_indexes = [compared_item[0] for compared_item in item2[2]]
        if item2[0] not in item1_compared_item_indexes and item1[0] not in item2_compared_item_indexes:
            print("Is", item1[1][1], "bigger than", f"{item2[1][1]}" + "?")
            item1_is_bigger = item1[1] > item2[1]
            l_enum[i][1][2].append((item2[0], item1_is_bigger))
        else:
            item2_is_in_item1 = False
            for compared_item in item1[2]:
                if compared_item[0] == item2[0]:
                    item2_is_in_item1 = True
                    item1_is_bigger = compared_item[1]

            if not item2_is_in_item1:
                for compared_item in item2[2]:
                    if compared_item[0] == item1[0]:
                        item1_is_bigger = not compared_item[1]

            if item1_is_bigger:
                print("Items were compared before.", item1[1][1], "was bigger than", f"{item2[1][1]}" + ".")
            else:
                print("Items were compared before.", item2[1][1], "was bigger than", f"{item1[1][1]}" + ".")

                    

        if item1_is_bigger:
            winners.append(l_enum[i])
        else:
            winners.append(l_enum[i2])
        
        i += 2
    
    return winners


def get_winner(l_enum):
    l_enum = copy.copy(l_enum)
    winners = l_enum
    while len(winners) > 1:
        winners = get_winners(winners)

    return winners[0]
    

def tournament_sort(l):
    l_sorted = []
    l_enum = list(enumerate(l))
    l_enum = [[i, val, []]for i, val in l_enum]
    l_enum2 = list(enumerate(l_enum))
    limit = len(l) - 1
    i = 0
    while i < limit:
        winner = get_winner(l_enum2)
        winner_i = winner[0]
        del l_enum2[winner_i]
        l_enum2_unenum = [item[1] for item in l_enum2]
        l_enum2 = list(enumerate(l_enum2_unenum))
        l_sorted.append(winner[1])
        i += 1

    comparisons = 0
    max_comperisons_per_item = 0
    l_sorted2 = []
    for item in l_sorted:
        item_comparisons_len = len(item[2])
        comparisons += item_comparisons_len
        if item_comparisons_len > max_comperisons_per_item:
            max_comperisons_per_item = item_comparisons_len
        l_sorted2.append(item[1])
    
    l_sorted2.reverse()
    return l_sorted2, comparisons, max_comperisons_per_item

count = 10
random_numbers = [(i, str(i)) for i in range(count)]
random.shuffle(random_numbers)
l_sorted = tournament_sort(random_numbers)
print("is sorted:", is_sorted(l_sorted[0]))
print("comparisons:", l_sorted[1])
print("max comparisons per item:", l_sorted[2])