"""
for element in range(9):
    print("*********")
"""

# 外层循环：控制行数
for element1 in range(1, 10):
    # 内层循环：控制列数
    for element2 in range(element1):
        # end 表示末尾的意思 end="" 表示不换行
        print("*", end="")
    print()
