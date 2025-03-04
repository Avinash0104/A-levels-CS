# ArrayNodes[20][3] : integer
ArrayNodes = [[-1 for i in range(0, 3)] for j in range(0, 10)]
RootPointer = 0
ArrayNodes[0] = [1, 20, 5]
ArrayNodes[1] = [2, 15, -1]
ArrayNodes[2] = [-1, 3, 3]
ArrayNodes[3] = [-1, 9, 4]
ArrayNodes[4] = [-1, 10,-1]
ArrayNodes[5] = [-1, 58, -1]
FreeNode = 6


def SearchValue(root, value):
    if root == -1:
        return -1
    else:
        if ArrayNodes[root][1] == value:
            return root
        else:
            if ArrayNodes[root][1] == -1:
                return -1
    if ArrayNodes[root][1] > value:
        return SearchValue(ArrayNodes[root][0], value)
    if ArrayNodes[root][1] < value:
        return SearchValue(ArrayNodes[root][2], value)

def PostOrder(root):
    if ArrayNodes[root][0] != -1:
        PostOrder(ArrayNodes[root][0])
    if ArrayNodes[root][2] != -1:
        PostOrder(ArrayNodes[root][2])
    print(ArrayNodes[root][1])

result = SearchValue(0, 15)
if result == -1:
    print("value was not found")
else:
    print("value is found at index", result)
PostOrder(0)

    




