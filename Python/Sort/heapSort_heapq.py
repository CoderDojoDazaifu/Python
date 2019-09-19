# ヒープソート（2分ヒープ）
# ヒープソートはheapqモジュールを使うと簡単に実装できる
# https://docs.python.org/ja/3/library/heapq.html

import heapq

# arr:配列
def heapSort(arr):
    srt = []
    for elm in arr:
        # 1つずつpushして
        heapq.heappush(srt, elm)
        # print(str(srt))
    # 1つずつpopする
    return [heapq.heappop(srt) for i in range(len(srt))]


# テスト
print(heapSort([8, 6, 1, 4, 2]))
print(heapSort([3, 6, 1, 4, 2]))
