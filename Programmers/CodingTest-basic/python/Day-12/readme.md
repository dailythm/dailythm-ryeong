# Day 12

---

## [045] 모음 제거 [🔎][045]

> 영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다.  
> 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

```python
def solution(my_string):
    answer = ''
    for i in my_string:
        if not (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            answer += i
    return answer
```

---

## [046] 문자열 정렬하기(1) [🔎][046]

> 문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.

```python
def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit() : answer.append(int(i))
    return sorted(answer)
```

---

## [047] 숨어있는 숫자의 덧셈 [🔎][047]

> 문자열 my_string이 매개변수로 주어집니다.  
> my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

```python
def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit() : answer += int(i)
    return answer
```

---

## [048] 소인수분해 [🔎][048]

> 소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다.  
> 예를 들어 12를 소인수 분해하면 2 _ 2 _ 3 으로 나타낼 수 있습니다.
> 따라서 12의 소인수는 2와 3입니다.  
> 자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

```python
def solution(n):
    answer = []
    for i in range(2, int(n // 2) +1):
        if n % i == 0: answer.append(i)
        while n % i == 0:
            n /= i
    if answer == [] : return [n]
    else : return answer
```

---

[045]: https://school.programmers.co.kr/learn/courses/30/lessons/120849
[046]: https://school.programmers.co.kr/learn/courses/30/lessons/120850
[047]: https://school.programmers.co.kr/learn/courses/30/lessons/120851
[048]: https://school.programmers.co.kr/learn/courses/30/lessons/120852
