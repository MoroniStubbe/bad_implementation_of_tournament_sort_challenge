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
        if l_enum[i][1][1] > l_enum[i2][1][1]:
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
    l_enum2 = list(enumerate(l_enum))
    limit = len(l) - 1
    i = 0
    while i < limit:
        winner = get_winner(l_enum2)
        winner_i = winner[0]
        del l_enum2[winner_i]
        l_enum2_unenum = [item[1] for item in l_enum2]
        l_enum2 = list(enumerate(l_enum2_unenum))
        l_sorted.append(winner[1][1])
        i += 1

    l_sorted.reverse()
    return l_sorted


random_numbers = [random.random() for _ in range(100)]
l_sorted = tournament_sort(random_numbers)
print(is_sorted(l_sorted))