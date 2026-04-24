number_list = [32, 5, 12, 8, 3, 75, 2, 15, 64]

# 初始化最大值为列表的第一个元素
max_number = number_list[0]
# 遍历列表
for i in range(1, len(number_list)):
    # 每次判断当前的最大值与当前遍历到的元素 谁大
    if max_number < number_list[i]:
        # 如果当前遍历到的元素大 则将当前元素赋给最大值
        max_number = number_list[i]

print("Le plus grand nombre est: " + str(max_number))