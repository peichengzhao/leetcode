from typing import List

def find_number(a: List[int]) -> int:
    res = set(a)
    updated = True
    while updated:
        updated = False
        # 遍历当前所有数的两两组合
        temp = list(res)  # 转列表固定遍历对象
        for x in temp:
            for y in temp:
                val = x & y
                if val not in res:
                    res.add(val)
                    updated = True
    return len(res)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    count = int(data[idx])
    idx += 1
    for _ in range(count):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        print(find_number(a))

if __name__ == "__main__":
    main()