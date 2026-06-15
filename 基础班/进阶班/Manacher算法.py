#Manacher算法
#解决回文问题

def manacher(str: str):
    if not str:
        return 0
    strx = "#" + "#".join(list(str)) + "#"
    p_arr = [0] * len(strx)
    r, c = -1, -1
    for i in range(len(strx)):
        p_arr[i] = min(p_arr[2 * c - i], r - i) if r > i else 1
        while i + p_arr[i] < len(strx) and i - p_arr[i] > -1:
            if strx[i + p_arr[i]] == strx[i - p_arr[i]]:
                p_arr[i] += 1
            else:
                break
        if i + p_arr[i] > r:
            r = i + p_arr[i]
            c = i
    return max(p_arr) - 1
