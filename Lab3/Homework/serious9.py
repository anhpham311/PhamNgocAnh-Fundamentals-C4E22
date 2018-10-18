l = [1,2,5,-10,9,6]
    
def get_even_list(l):
    for i in l:
        if i % 2 == 0:
            pass
        else:
            l.remove(i)
    return l

print(get_even_list(l))
