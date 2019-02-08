import random

import math

listes = []
"""for i in range(3):
    # listes.append(random.sample(range(5, 50), random.randint(5,1000)))
    listes.append(random.sample(range(1, 100), 10))
"""

listes = [
    [10,20,30,90,30,54,123,34,656,246,24,842,6784,2,56,4,5,7423,6,6,3,345,6,7,345,46],
    [10,20,30,90],
    [10,20,30,90,30,54,123,34,656,246,24,842,6784,2,56,4]
          ]


def sum(liste):
    total = 0
    for x in liste:
        total += x

    return total


def mean(liste):
    total = sum(liste)
    return total / len(liste)


def std(liste):
    meann = mean(liste)
    total = 0.0
    for x in liste:
        total += (meann - x) ** 2

    return math.sqrt(total / (len(liste) - 1))


def variance(samples):
    M = 0
    S = 0
    index = 0
    for x in samples:
        x = samples[index]
        oldM = M
        M = M + (x - M) / (index + 1)
        S = S + (x - M) * (x - oldM)
        if index != 0:
            print("---- {}".format(S/(index+1-1)))
        index += 1
    return S / (len(samples) - 1)


def evaluate(nums):
    print("list: ")
    print(nums)
    print("sum: {}".format(sum(nums)))
    print("mean: {}".format(mean(nums)))
    print("size: {}".format(len(nums)))

    batch_std = std(nums)
    print("batch_std: {}".format(batch_std))

    streaming_std = variance(nums)
    print("streaming_std: {}".format(streaming_std))

    difference = batch_std - streaming_std
    print("batch_std - streaming_std = {}".format(difference))
    error = 100 * (difference / batch_std)
    print("original error: {}%".format((error)))
    print("float error: {}%".format(float("%0.9f" % error)))
    print("int error: {}%".format(int(error)))
    print("\n")

def main():

    #for liss in listes:

    liss = listes[0]
    print("liste:{}".format(liss) )
    """
    for i in range(len(liss)):
        if i==0 or i==1:
            continue
        sub_liste = liss[:i]
        print("original: {}".format(std(sub_liste)))
    """
    for i in range(len(liss)):
        if i == 0 or i == 1:
            continue
        sub_liste = liss[:i]
        print("original: {}".format(std(sub_liste)))
        evaluate(sub_liste)

    for liste in listes:
        evaluate(liste)
#main()

"""
for i in range(len(listes[0])):
    if i == 0 or i == 1:
        continue
    sub_liste = listes[0][:i]
    print("original[{}] S: {} - standardization: {}".format(i,std(sub_liste)))
"""

i = 0
for x in listes[0]:
    i += 1
    if i == 1:
        continue
    print("standardization({}) : {}".format(x, ((x-mean(listes[0][:i]))/(std(listes[0][:i])))))

M = S = count = sum = 0
while(True):
    val = input("sayı: ")
    val = int(val)
    sum += val
    count += 1
    oldM = M
    M = M + (val - M) / (count)
    S = S + (val - M) * (val - oldM)
    if count != 1:
        print("S = {}".format(S / (count - 1)))
        print("stream standardization({}) : {}".format(val, (val-(sum/count))/math.sqrt(S/(count-1))))
