import random
#code to flip a single bit in a bitstring.


def corrupt(data):
    data_list = list(data)
    rand = random.randint(1, len(data))
    data_list[-rand] = str(int(data_list[-rand]) ^ 1)

    data = ''.join(map(str, data_list))

    return data
