# ヒープソート（2分ヒープ）
# arr:配列
def heapSort(arr):
    # パラメータの配列の長さ
    n = len(arr)
    i = 0

    while(i < n):
        # ヒープを構成する
        upheap(arr, i)
        i += 1

        print("UP:" + str(arr))

    while(i > 1):
        # ヒープから最大値を取り出す
        i -= 1
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp

        # ヒープを再構成する
        downheap(arr, i - 1)

        print("DOWN:" + str(arr))

    return arr


def upheap(arr, n):
    while n != 0:
        parent = int((n - 1) / 2)
        if arr[n] > arr[parent]:
            # 大きな方を親にする
            arr[n], arr[parent] = arr[parent], arr[n]
            n = parent
        else:
            break


def downheap(arr, n):
    if n == 0:
        return

    parent = 0
    while True:
        # arr[n]の子要素
        child = 2 * parent + 1
        if child > n:
            break

        if child < n and arr[child] < arr[child + 1]:
            child += 1

        if arr[parent] < arr[child]:
            # 子要素の方が大きい場合、入替
            arr[child], arr[parent] = arr[parent], arr[child]
        else:
            break


# テスト
print(heapSort([8, 6, 1, 4, 2]))
print(heapSort([3, 6, 1, 4, 2]))
