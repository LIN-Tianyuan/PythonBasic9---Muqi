import random

my_collection = ['rouge', 'rose', 'orange', 'rouge',
                 'rose', 'jaune', 'rose', 'jaune']
bag_of_balls = ['rose', 'bleu', 'vert', 'orange',
                'rouge', 'pourpre', 'vert', 'bleu',
                'bleu', 'rouge', 'vert', 'poupre',
                'jaune', 'rouge', 'rose', 'rouge',
                'vert', 'jaune']
balls_outputs = []

"""
for i in range(5):
    pick = random.randint(0, 17)
    ball = bag_of_balls[pick]
    selection = random.choice(bag_of_balls)
    print(ball)
    if ball == "vert":
        my_collection.append(ball)
        print("Bravo! Vous avez réussit!")
        break
        
print("Ce sont tout vos pioches! Vous n'avez pas réussit d'obtenir une bille vert!")
"""

# 初始化抽球的次数
remaining_draws = 5
for i in range(remaining_draws):
    # 随机抽球
    selection = random.choice(bag_of_balls)
    # 每次抽完球，把球加到balls_outputs里
    balls_outputs.append(selection)
    if selection == "vert":
        # 抽到绿球后，加到my_collections里
        my_collection.append(selection)
        print("Bravo! Vous avez réussit!")
        print("Il restait " + str(remaining_draws - i - 1) + " tirages.")
        break

# 最后my_collection里没有绿球的话，说明游戏失败
if "vert" not in my_collection:
    print("Ce sont tout vos pioches! Vous n'avez pas réussit d'obtenir une bille vert!")

print("Billes sorties pour ce tirage: ")
print(balls_outputs)
print("La nouvelle collection contient: ")
print(my_collection)