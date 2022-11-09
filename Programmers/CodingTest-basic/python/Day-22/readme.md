# Day 22

---

## [085] 저주의 숫자 3 [🔎][085]

> 3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다.  
> 3x 마을 사람들의 숫자는 다음과 같습니다.

| 10진법 | 3x 마을에서 쓰는 숫자 | 10진법 | 3x 마을에서 쓰는 숫자 |
| :----- | :-------------------- | :----- | :-------------------- |
| 1      | 1                     | 6      | 8                     |
| 2      | 2                     | 7      | 10                    |
| 3      | 4                     | 8      | 11                    |
| 4      | 5                     | 9      | 14                    |
| 5      | 7                     | 10     | 16                    |

> 정수 n이 매개변수로 주어질 때, n을 3x 마을에서 사용하는 숫자로 바꿔 return하도록 solution 함수를 완성해주세요.

```python
def solution(n):
    answer = 0
    count = 0
    while count < n:
        answer += 1
        count += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer
```

---

## [086] 평행 [🔎][086]

> 점 네 개의 좌표를 담은 이차원 배열 dots가 다음과 같이 매개변수로 주어집니다.

- [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]

> 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.

```python
def solution(dots):
    inc = []
    for i in range(0, 4):
        for j in range(i+1, 4):
            inc.append((dots[i][0]-dots[j][0])/(dots[i][1]-dots[j][1]))
    checkLis = set(inc)
    for i in checkLis:
        if inc.count(i) > 1: return 1
    return 0
```

---

## [087] 겹치는 선분의 길이 [🔎][087]

> 빨간색, 초록색, 파란색 선분이 x축 위에 있습니다.  
> 세 선분의 x좌표 시작과 끝이 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때,
> 두 개 이상의 선분이 겹치는 부분의 길이를return 하도록 solution 함수를 완성해보세요.

```python
def solution(lines):
    answer = 0
    pointList = []
    for i in lines:
        for j in range(i[0],i[1]):
            pointList.append(j)
    numList = set(pointList)
    print(numList)
    for i in numList:
        if pointList.count(i) > 1 : answer += 1
    return answer
```

---

## [088] 유한소수 판별하기 [🔎][088]

> 소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 합니다.
> 분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 합니다.
> 유한소수가 되기 위한 분수의 조건은 다음과 같습니다.

- 기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.

> 두 정수 a와 b가 매개변수로 주어질 때, a/b가 유한소수이면 1을, 무한소수라면 2를 return하도록 solution 함수를 완성해주세요.

```python
def solution(a, b):
    answer = 0
    for i in range(min(a,b), 0, -1):
        if a % i == 0 and b % i == 0:
            a, b = a // i, b // i
    while True:
        if b % 2 == 0: b = b // 2
        elif b % 5 == 0: b = b // 5
        else : break
    if b == 1 : return 1
    return 2
```

---

[085]: https://school.programmers.co.kr/learn/courses/30/lessons/120871
[086]: https://school.programmers.co.kr/learn/courses/30/lessons/120875
[087]: https://school.programmers.co.kr/learn/courses/30/lessons/120876
[088]: https://school.programmers.co.kr/learn/courses/30/lessons/120878
