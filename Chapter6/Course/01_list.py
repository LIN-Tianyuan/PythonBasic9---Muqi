# 创建列表（list）
# 列表里的东西叫做元素（element）
# 元素与元素之间用逗号相隔
leisure = ['swim', 'dance', 'sing']
print(leisure)
print("--------------------")
# 获取列表的长度（元素个数）※
# length
print(len(leisure))
print("--------------------")
# 测试元素是否在列表里
print('basketball' in leisure)
print('dance' in leisure)
print('DANCE' in leisure)
print("--------------------")
# 获取元素的下标（index）
print(leisure.index('swim'))
print("--------------------")
# 获取列表中的元素  ※ （查）
print(leisure[0])
print(leisure[1])
print("--------------------")
# 修改列表中的元素  ※ （改）
leisure[0] = 'ski'
print(leisure[0])
print(leisure)
print("--------------------")
# 增加元素 第一种：到列表末尾 ※ （增）
leisure.append("game")
print(leisure)
# 增加元素 第二种：添加到任意位置 ※ （增）
leisure.insert(3, "climb")
print(leisure)
print("--------------------")
# 删除元素 第一种：删除指定元素（提供元素名） ※ （删）
leisure.remove("climb")
print(leisure)
# 删除元素 第二种：删除指定下标元素（提供下标index）※ （删）
leisure.pop(1)
print(leisure)
print("--------------------")
# 清空列表
leisure.clear()
print(leisure)
print("--------------------")

month = ["Janvier", "Février", "Mars"]
season = ["Automne", "Hiver", "Printemps", "Eté"]
"""
# 拼接两个列表
various_times = month + season
print(month)
print(season)
print(various_times)
"""

# 把另一个列表的所有元素拼接到本列表后面
month.extend(season)
print(month)
print(season)
print("--------------------")

rainbow = ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo', 'violet']
print(rainbow)
print(len(rainbow))
# 切片 取前不取后
print(rainbow[1:4])
# 如果要一直取到列表最后的元素 就可以省略切片的结束index
print(rainbow[3:])  # print(rainbow[3:8])
# 如果要从列表开头取元素 可以省略切片的开始index
print(rainbow[:6])  # print(rainbow[0:6])
print(rainbow[:])   # print(rainbow[0:8])
print("--------------------")
print(rainbow[-1])  # print(rainbow[6])
print(rainbow[2:6])
print(rainbow[-5:-1])











