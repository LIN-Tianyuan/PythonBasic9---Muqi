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

# 默认参数
def season_pref(season="Eté"):
    print("Ma saison préférée est " + season + ".")

# season_pref("Eté")
season_pref()
season_pref("Hiver")