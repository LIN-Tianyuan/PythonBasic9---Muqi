# 取左不取右
# range(11): 0 - 10
# 如果只有一个数 就是从0开始 直到这个数的前一位
for element in range(11):
    print(element)

print("----------")
for element in range(1, 11):
    print(element)

print("----------")
# range(开始，结束，步长）
for element in range(1, 10, 2):
    print(element)