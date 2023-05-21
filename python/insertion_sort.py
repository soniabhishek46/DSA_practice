


def insertion_sort(l: list):
    #import pdb; pdb.set_trace()

    n = len(l)
    for j in range(1, n):
        i = j - 1
        temp = l[j]
        # if first condition is '>' then it sorts in ascending order
        # elseif condition is '<' then it sorts in descending order.
        while((l[i] > temp) and (i >= 0)):
            l[i+1] = l[i]
            i -= 1
        
        l[i+1] = temp
        
        print(l)




if __name__ == '__main__':
    l = [4, 7, 2, 5, 9, 3, 1]
    print(l)
    insertion_sort(l)
    print(l)