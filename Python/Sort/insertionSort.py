# 挿入ソート
# arr:配列
def insertionSort(arr):
    # パラメータの配列の長さ
    n = len(arr)

    # 添字1から最後までループする
    for i in range(1, n):
        print(str(arr))

        key = arr[i]

        j = i - 1
        # iより小さい添字を降順に比較し、挿入する位置を決める
        while j >= 0 and key < arr[j]:
            # 大きければずらす
            arr[j + 1] = arr[j]
            j -= 1

        print(str(key) + "が挿入される位置は" + str(j + 1) + "です")
        arr[j + 1] = key

    return arr

# テスト
print(insertionSort([8, 6, 1, 4, 2]))
