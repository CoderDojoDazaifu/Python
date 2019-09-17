# 選択ソート
# arr:配列
def selectionSort(arr):
    # パラメータの配列の長さ
    n = len(arr)

    print("ソート前:" + str(arr))

    # パラメータの配列の長さ-1回ループする（最後の1つは自然に決まるので-1）
    for i in range(n - 1):

        # iの要素以降で一番小さい数のindexを選択し、iと入れ替える
        num = arr[i:].index(min(arr[i:]))
        print(str(i) + "以降で一番小さい数は" + str(arr[i + num]) + "で、")
        arr[i], arr[i + num] = arr[i + num], arr[i]
        print("入れ替えると" + str(arr) + "になります")
    return arr

# テスト
print(selectionSort([8, 6, 1, 4, 2]))
