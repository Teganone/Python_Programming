def anagrams(strs):
    results = []
    while strs:
        word = strs.pop(0)
        print(f"核对：'{word}'在{[word]+strs}")
        same = list(filter(lambda x: sorted(x) == sorted(word), strs))
        results.append([word] + same)
        for w in same:
            strs.remove(w)
        print(f"相同：{[word]+same}")
        print(f"不同：{strs}")
    return results

# 调用函数的代码
lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(f'原始：{lst}\n')
print(f'结果：{anagrams(lst)}')