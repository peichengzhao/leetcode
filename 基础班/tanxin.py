
# 暴力解法  回溯DFS


def find_min_light(path: list[str]):
    if path == None or len(path) ==0:
        return 0
    light = 0
    for index in range(len(path)):
        if path[index] == "x":
            index += 1
        else:
            if index + 1 ==len(path):
                break
            else:
                if path[index + 1] == "x":
                    index += 2
                else:
                    light += 1
                    index += 2
    return light

# 分割金条
# 一个金条，分割成若干段，每段的价值是金条本身的价值
def find_min_cut(hope: list[int]):
    sorted_hope = sorted(hope)
    result = 0
    for index in range(len(sorted_hope) - 1):
        temp = sorted_hope[index] + sorted_hope[index + 1]
        result += temp
        sorted_hope[index + 1] = temp
    return result

# 做项目
# 一个项目有投入和收益，投入和收益都是正数
# 给定一个项目列表，给定一个初始资金w，给定一个最大投资次数k，求最大收益v
def get_max_profit(projects: list[tuple[int, int]], w: int, k: int):
    if projects == None or len(projects) == 0:
        return 0
    w_start = w
    cost_sorted_projects = sorted(projects, key=lambda x: x[0])
    profit_sorted_projects = []
    for index in range(k-1):
        temp = 0    
        while cost_sorted_projects and cost_sorted_projects[temp][0] <= w:
            temp += 1
            profit_sorted_projects.append(cost_sorted_projects.pop(0))
        profit_sorted_projects.sort(key=lambda x: x[1], reverse=True)
        w += profit_sorted_projects[0][1]
        profit_sorted_projects.pop(0)
    return w - w_start
#并查集



