# # from bitarray import bitarray

# # # 创建长度为10的位图，初始全0
# # b = bitarray(10)
# # b.setall(0)

# # # 设置位
# # b[2] = 1  # 第2位设为1
# # b[5] = 1  # 第5位设为1
# # # 检查位
# # print(b[2])  # True
# # print(b[3])  # False
# # # 位运算
# # b2 = bitarray(10)
# # b2[5] = 1
# # b2[7] = 1
# # print(b | b2)  # 按位或：[0,0,1,0,0,1,0,1,0,0]
# # print(b & b2)  # 按位与：[0,0,0,0,0,1,0,0,0,0]
# # # 统计1的个数
# # print(b.count())  # 2


# # import numpy as np
# # # 创建长度为2的uint8数组（共16位），初始全0
# # bitmap = np.zeros(2, dtype=np.uint8)
# # print(bitmap)
# # # 设置第3位（第一个字节的第3位）
# # bitmap[0] |= 1 << 3
# # # 设置第9位（第二个字节的第1位）
# # bitmap[1] |= 1 << 1
# # # 检查第3位
# # print((bitmap[0] & (1 << 3)) != 0)  # True
# # # 检查第9位
# # print((bitmap[1] & (1 << 1)) != 0)  # True


# from ast import mod


# a = 2983746895
# result_1 = a // 2
# result_2 = a >> 1
# print(result_1, result_2)
# print(result_1 == result_2)


# b = 170
# result_1 = b % 64
# result_2 = b & 63
# print(result_1, result_2)
# print(result_1 == result_2)




from openai import OpenAI

client = OpenAI(api_key="sk-G5RXRsf9mwPFLAbVpiwt5xUEkA6CD197Mhj80VC3RIQg4qK0", base_url="https://api.deepbricks.ai/v1/")
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"},
        {"role": "tool", "content": "aaaasdadasada.", "tool_call_id": "123"}
    ],
)

print(response.choices[0].message.content)