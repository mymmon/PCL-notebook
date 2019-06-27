## 相似度评价值

- **欧几里得距离**
    - 指多维空间中两点间的距离
    - 适用于数据较为**规范**的时候
    - 计算两个用户之间的**距离**
    - 对距离进行 + 1 并求其**倒数**
    - 计算公式 
```tex
\sqrt{(p_1-q_1)^2+(p_2-q_2)^2+...+(p_n-q_n)^2} = \sqrt{\sum_{i=1}^{n}(p_i-q_i)^2}
```

```python
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

- **皮尔逊相关系数**
    - 度量两个变量间相关程度的方法
    - 在数据**不规范**的时有更好的表现
    - 了解变量的总体变化情况
    - 计算公式 
```tex
r = {\sum XY - \sum{X} \sum {Y} \over N} \over \sqrt{\left( \sum {X^2} - (\sum X)^2\over N  \right)- \left( \sum {Y^2} - (\sum Y)^2\over N  \right)}
```

```python
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
```