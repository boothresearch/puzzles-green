def score(x, y):
    distance=(x**2+y**2)**0.5
    if distance>10:
       reward=0 
    elif distance<=10 and distance>5:
       reward=1
    elif distance<=5 and distance>1:
        reward=5
    elif distance<=1:
        reward=10

    return reward
