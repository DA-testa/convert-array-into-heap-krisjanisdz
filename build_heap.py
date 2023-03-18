# python3


def build_heap(data, n):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, swaps)



    return swaps

def heapify(data, n, i, swaps):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    mazakais = i

    if lchild < n and data[lchild] < data[mazakais]:
        mazakais = lchild

    if rchild < n and data[rchild] < data[mazakais]:
        mazakais = rchild

    if i != mazakais:
        data[i], data[mazakais] = data[mazakais], data[i]
        swaps.append((i,mazakais))
        heapify(data, n, mazakais, swaps)

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    ievade = input()
    if 'I' in ievade:
        n = int(input())
        data = list(map(int, input().split()))
       

    if 'F' in ievade:
        file = input()
        with open ("./test/"+file,'r') as fails:
            n = int(fails.readline())
            data = list(map(int,fails.readline().split()))


    # input from keyboard
    

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data,n)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
