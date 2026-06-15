def radix_sort(arr):
    """
    基数排序（LSD 最低位优先）
    :param arr: 待排序的整数数组（仅支持非负整数，若需支持负数可先偏移再排序）
    :return: 排序后的数组
    """
    if not arr:  # 处理空数组
        return arr
    
    # 步骤1：找到数组中的最大值，确定最大位数
    max_num = max(arr)
    digit = 1  # 初始处理个位（除数为1）
    
    # 步骤2：依次处理每一位（个位、十位、百位...）
    while max_num // digit > 0:
        # 对当前位执行稳定的计数排序
        counting_sort_for_radix(arr, digit)
        digit *= 10  # 处理下一位（除数×10）
    
    return arr

def counting_sort_for_radix(arr, digit):
    """
    针对基数排序的计数排序（按当前位排序）
    :param arr: 待排序数组
    :param digit: 当前处理的位数（1=个位，10=十位，100=百位...）
    """
    n = len(arr)
    output = [0] * n  # 存储排序后的临时数组
    count = [0] * 10  # 计数数组（0-9 共10个数字）
    
    # 步骤1：统计当前位上每个数字（0-9）的出现次数
    for num in arr:
        # 提取当前位的数字（比如digit=10时，num=589 → (589//10)%10 = 8）
        current_digit = (num // digit) % 10
        count[current_digit] += 1
    
    # 步骤2：计算前缀和，确定每个数字在output中的结束位置（保证稳定性）
    for i in range(1, 10):
        count[i] += count[i-1]
    
    # 步骤3：逆序遍历原数组，将元素放入output的对应位置（逆序保证稳定）
    for num in reversed(arr):
        current_digit = (num // digit) % 10
        count[current_digit] -= 1  # 先减1得到起始位置
        output[count[current_digit]] = num
    
    # 步骤4：将排序后的临时数组复制回原数组
    arr[:] = output

# 测试示例
if __name__ == "__main__":
    # 测试用例1：普通整数数组
    test_arr1 = [170, 45, 75, 90, 802, 24, 2, 66]
    radix_sort(test_arr1)
    print("排序结果1：", test_arr1)  # 输出：[2, 24, 45, 66, 75, 90, 170, 802]
    
    # 测试用例2：包含0和重复元素
    test_arr2 = [0, 5, 3, 5, 9, 0, 12]
    radix_sort(test_arr2)
    print("排序结果2：", test_arr2)  # 输出：[0, 0, 3, 5, 5, 9, 12]