# クイックソート
# arr:配列
def quickSort(arr):
    if len(arr) < 2:
        return arr

    i = arr[0]
    # 基準値の決め方に性能が左右されるため、ranom.choice(arr)を用いる方法もある
    count = 0

    left = []
    right = []

    # 基準値より大小で分割
    for elm in arr:
        if elm < i:
            left.append(elm)
        elif elm > i:
            right.append(elm)
        else:
            count += 1

    print(str(left) + str(right))

    # 再帰
    left = quickSort(left)
    right = quickSort(right)

    #print(left + [i] * count + right)
    return left + [i] * count + right

# テスト
print(quickSort([8, 6, 1, 4, 2]))
