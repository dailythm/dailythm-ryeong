# Day 7

---

## [025] 특정 문자 제거하기 [🔎][025]

> 문자열 my_string과 문자 letter이 매개변수로 주어집니다.  
> my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

```python
def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if not i == letter:
            answer += i
    return answer
```

---

## [026] 각도기 [🔎][026]

> 각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다.  
> 각 angle이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.

```python
def solution(angle):
    if angle < 90 :
        return 1
    elif angle == 90 :
        return 2
    elif angle < 180 :
        return 3
    else : return 4
```

---

## [027] 양꼬치 [🔎][027]

> 머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다. 양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다.  
> 정수 n과 k가 매개변수로 주어졌을 때, 양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요.

```python
def solution(n, k):
    return n * 12000 + (k - n // 10) * 2000
```

---

## [028] 짝수의 합 [🔎][028]

> 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

```python
def solution(n):
    answer = 0
    for i in range(2, n+1, 2):
        answer += i
    return answer
```

---

[025]: https://school.programmers.co.kr/learn/courses/30/lessons/120826
[026]: https://school.programmers.co.kr/learn/courses/30/lessons/120829
[027]: https://school.programmers.co.kr/learn/courses/30/lessons/120830
[028]: https://school.programmers.co.kr/learn/courses/30/lessons/120831
