import copy

def list(some_list):

    a = copy.copy(some_list)
    b = ''
    
    for i in range(len(a)-1):
        c = str(a[i]) + ', '
        b += c
    return b + 'and ' + str(a[-1])

# spam = ['apples', 'bananas', 'tofu', 'cats']
spam = [1.1, 2.2, 3, 'four']
print(list(spam))
print(spam)