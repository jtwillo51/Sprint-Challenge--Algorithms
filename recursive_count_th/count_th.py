'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    
    check = word[0:1]
    if check == "th":
        count += 1
    else: 
        count_th(word[2:])
    return count