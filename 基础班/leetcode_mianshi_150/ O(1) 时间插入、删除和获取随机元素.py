import random


class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.length = 0

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False
        self.hash_map[val] = True
        self.length += 1
        return True        

    def remove(self, val: int) -> bool:
        if val in self.hash_map:
            self.hash_map.popitem(val)
            self.length -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        import random
        random_value = random.random(0, self.length)
        for key,value in self.hash_map:
            if key == random_value:
                return key
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()








import random

class RandomizedSet:

    def __init__(self):
        self.nums = []  # 列表：存储所有元素，支持随机访问
        self.val_to_idx = {}  # 哈希表：值 -> 列表索引

    def insert(self, val: int) -> bool:
        # 元素已存在，返回False
        if val in self.val_to_idx:
            return False
        # 追加到列表末尾，记录索引
        self.val_to_idx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        # 元素不存在，返回False
        if val not in self.val_to_idx:
            return False
        # 核心：O(1)删除列表元素 → 用最后一个元素覆盖待删除元素
        idx = self.val_to_idx[val]  # 待删除元素的索引
        last_num = self.nums[-1]    # 列表最后一个元素
        
        # 1. 替换元素
        self.nums[idx] = last_num
        # 2. 更新哈希表中最后一个元素的索引
        self.val_to_idx[last_num] = idx
        # 3. 删除列表最后一个元素
        self.nums.pop()
        # 4. 删除哈希表中待删除元素
        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:
        # O(1) 随机返回一个元素（最优写法）
        return random.choice(self.nums)