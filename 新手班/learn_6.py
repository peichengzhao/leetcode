import numpy as np
import os

array = [2, 3, 5, 1, 12, 34, 4, 6,3, 7, 80, 12, 342, 12, 231]

def look_list(array:list):
    for i in range(len(array)):
        print(array[i], end=' ')
    print('\n')

class Student():
    def __init__(self, name:str, id:str, age:int):
        self.name = name
        self.id = id
        self.age = age
    

student_1 = Student("张三", "123456", 20)
student_2 = Student("李四", "123457", 19)
student_3 = Student("王五", "123458", 22)
student_4 = Student("赵六", "123459", 12)
student_5 = Student("孙七", "123460", 9)
student_6 = Student("周八", "123461", 55)
student_7 = Student("吴九", "123462", 54)
student_8 = Student("郑十", "123463", 4)


students = [student_1, student_2, student_3, student_4, student_5, student_6, student_7, student_8]

def look_students(students:list):
    for student in students:
        print(student.name, student.id, student.age)
    print('\n')


# 比较器

def compare_id(student1: Student, student2: Student):
    if student1.id <= student2.id: # 第一个参数排在前面
        return -1
    else:
        return 1
def compare(students:list):
    look_students(students)
    print("==================")
    sorted_students = sorted(students, key=lambda x: x.age, reverse=True)
    look_students(sorted_students)
    print("==================")



import heapq
min_heap = []

heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 8)
heapq.heappush(min_heap, 1)
print("当前小根堆:", min_heap)  # 输出: [1, 2, 8, 5]（注意：列表并非完全排序，但堆顶是最小的）
print("堆顶元素（最小）:", min_heap[0])  # 输出: 1（直接取索引0，不弹出）

# 弹出堆顶元素（heappop：弹出最小元素，且重新维护堆结构）
smallest = heapq.heappop(min_heap)
print("弹出的最小元素:", smallest)  # 输出: 1
print("弹出后堆:", min_heap)        # 输出: [2, 5, 8]
# ========== 方式2：直接将列表堆化（原地操作） ==========
nums = [9, 3, 7, 1, 4]
heapq.heapify(nums)  # 堆化后成为小根堆，原地修改
print("堆化后的列表（小根堆）:", nums)  # 输出: [1, 3, 7, 9, 4]

#实现大根堆
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -8)
heapq.heappush(max_heap, -1)
print("当前大根堆:", max_heap)
print("堆顶元素（最大）:", -max_heap[0])

max_heap = [-x for x in max_heap]
heapq.heapify(max_heap)
print("堆化后的列表（大根堆）:", max_heap)
print("堆顶元素（最大）:", -max_heap[0])
print("弹出的最大元素:", -heapq.heappop(max_heap))
print("弹出后堆:", max_heap)


# 学生堆
class StudentHeap():
    def __init__(self, students:list):
        self.student = []
        self.heap = []
    def push(self, student: Student):
        heapq.heappush(self.heap, student.age)
    def pop(self):
        return heapq.heappop(self.heap)



def compare_string():
    str1 = "abc"
    str2 = "abd"
    if str1 <= str2:
        return -1
    else:
        return 1
test = compare_string()
print(test)