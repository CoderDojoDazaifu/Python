# 分布数え上げ（カウント）ソート
# arr:配列
def countSort(arr):
    # 一番小さい数と大きい数
    num_min = min(arr)
    num_max = max(arr)
    # 分布格納用の配列を準備する
    count = [0] * (num_max - num_min + 1)

    # 分布を格納
    for elm in arr:
        count[elm - num_min] += 1

    return [elm for elm, i in enumerate(count, start=num_min) for __ in range(i)]

# テスト
print(countSort([8, 6, 1, 3, 3, 4, 2]))
