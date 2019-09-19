# バブルソート
# arr:配列
def bubbleSort(arr):
    # パラメータの配列の長さ
    n = len(arr)

    # パラメータの配列の長さ分ループする
    for i in range(n):

        # 要素をペアで順に比較する（ので-1）
        # iが増えるたび、最後の要素から降順に値が決まっていく（-i）
        for j in range(0, n - i - 1):

            print(str(arr[j]) + "と" + str(arr[j + 1]) + "を比べる")

            if arr[j] > arr[j + 1]:
                # 次の要素の値より大きかったら、入れ替える
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# テスト
print(bubbleSort([8, 6, 1, 4, 2]))
