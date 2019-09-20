# マージソート
# arr:配列
def mergeSort(arr):
    # パラメータの配列の長さ
    n = len(arr)
    if n < 2:
        return arr

    # 配列を分割する
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]
    print("Split:" + str(left) + str(right))

    # 再帰
    left = mergeSort(left)
    right = mergeSort(right)

    # 結合して返す
    return merge(left, right)


def merge(left, right):
    merged = []
    l, r = 0, 0

    # それぞれソート済みのため、左から順に見ていけばよい
    while l < len(left) and r < len(right):
        # ここで=でも比較することで、安定性を保っている
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1

    # 上のwhileはleftかrightのいずれかがFalseになった場合に終了するので、残り分をextendする
    if l < len(left):
        merged.extend(left[l:])
    if r < len(right):
        merged.extend(right[r:])
    print("Merge:" + str(merged))

    return merged


# テスト
print(mergeSort([8, 6, 1, 4, 2]))
