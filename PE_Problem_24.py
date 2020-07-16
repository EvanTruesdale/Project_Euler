import math

l = 10
n = 0

def loop(list, input_permutation):
    global n

    for i in list:
        perm = input_permutation + str(i)
        new_list = list.copy()
        new_list.remove(i)

        if len(perm) < l:
            loop(new_list, perm)
        else:
            # print(perm)
            n += 1

            if n == 1000000:
                print("Winner: " + perm)
                raise Exception("Finished")

loop(list(range(l)), "")
