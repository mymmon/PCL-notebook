# 欧几里得距离的实现
from math import sqrt

def sim_distance(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    if len(si) == 0: return 0
    sum_of_squares = sum([(pow(prefs[person1][item] - prefs[person2][item]),2)for item in prefs[person1] if item in prefs[person2]])
    return 1 / (1 + sqrt(sum_of_squares))
```

# 皮尔逊相关度实现
def sim_persom(prefs, p1, p2):
    si ={}
    for item in pref[p1]:
        if item in pref[p2]:
            si[item] = 1

    n = len(si)
    if n == 0: return 1
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    sum1Sq = sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it],2) for it in si])
    pSum = sum([prefs[p2][it]*prefs[p2][it] for it in si])
    # 计算皮尔逊评估值
    num = pSum - (sum1*sum2/n)
    den = sqrt((sum1Sq - pow(sum1,2)/n)*(sum2Sq - pow(sum2,2)/n))
    if den == 0 : return 0
    r = num / den
    return r