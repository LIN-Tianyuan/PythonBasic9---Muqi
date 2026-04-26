# 定义函数
"""
def greet():
    print("Salut, Terrien!")
"""

"""
# 定义函数
# 有一个形式参数 name
def greet(name):
    print("Salut, " + name + "!")

# 调用函数
# 函数调用时需要传入实际参数
greet("Terrien")
greet("Alex")
greet()
"""

"""
# 默认参数
def season_pref(season="Eté"):
    print("Ma saison préférée est " + season + ".")

# season_pref("Eté")
season_pref()
season_pref("Hiver")
"""

"""
# 不定参数
def visit(*countries):
    for country in countries:
        print("J'ai visité ce pays: " + country + ".")

visit("France", "Japon")
visit("Chine")
visit("Espagne", "Italie", "Allemagne")
"""

"""
leisure = ['swim', 'dance', 'sing']
print(leisure)
"""
# 第一种遍历
"""
for i in range(len(leisure)):
    print(leisure[i])
"""
"""
i = 0
while i < len(leisure):
    print(leisure[i])
    i = i + 1
"""
"""
# 第二种遍历 for对容器的简易操作
for i in leisure:
    print(i)
"""

def list_game(competitor_1, competitor_2, competitor_3):
    print("Concurrents du jour: " + competitor_1 + ", " + competitor_2 + ", " + competitor_3)

# 位置参数
list_game("alex", "bob", "charlie")
# 关键字参数
list_game(competitor_2="alex", competitor_1="bob", competitor_3="charlie")