from random import random

def parse_url(SERVER):
    temp = SERVER.split(':')
    if len(temp) != 1:
        port = int(temp[1])
    else:
        port = 6667
    return temp[0], port

def random_list(n=10):
    temp = list(range(n))
    result = []
    while len(temp) > 0:
        idx = int(random() * len(temp))
        result.append(temp[idx])
        del temp[idx]
    return result

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
