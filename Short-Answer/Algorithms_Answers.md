#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) linear


b) quadratic


c) exponential

## Exercise II

def egg_drop(eggs, n_floors):
    floor = n_floors//2
    prev_floor = floor -1
    next_floor = floor + 1
    
    if next_floor.egg == broken and floor.egg == safe:
        return floor
    elif floor.egg == broken:
        floor = floor -1
    elif floor.egg == safe:
        floor = floor + 1

run time of the above psudocode is log(n) because I am essentially doing a binary search

