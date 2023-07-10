from os import *
from sys import *
from collections import *
from math import *

from typing import *

def minimizeIt(arr: List[int], k: int) ->int:
    decreased = []
    increased = []

    for i in range(len(arr)):
        increased.append(arr[i] + k)
        if arr[i] - k < 0:
            decreased.append(arr[i] + k)
        else:
            decreased.append(arr[i] - k)

    minimum = min(min(increased), min(decreased))
    maximum = min(max(increased), max(decreased))

    return maximum - minimum
