def hudielueyuan(n: int, s: str):
    left_list = {}
    right_list = {}
    s = list(s)
    for i in range(len(s)):
        if s[i] in right_list:
            right_list[s[i]] += 1
        else:
            right_list[s[i]] = 1
    for i in range(len(s)):
        temp = s[i]
        if temp in right_list:
            right_list[temp] -= 1
        left_number = left_list[s[i]] if s[i] in left_list else 0
        right_number = right_list[s[i]] if s[i] in right_list else 0
        if left_number == right_number:
            s[i] = chr((ord(s[i]) - ord("a")+ 1)% 26 + ord("a"))
        if s[i] in left_list:
            left_list[s[i]] += 1
        else:
            left_list[s[i]] = 1
    return "".join(s)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = str(input())
        print(hudielueyuan(n, s))

if __name__ == "__main__":
    main()


