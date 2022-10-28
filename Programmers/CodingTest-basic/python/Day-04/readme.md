# Day 3

---

## [013] 피자 나눠 먹기(1) [🔎][013]

> 머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다.  
> 피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를
> **한 조각 이상** 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.

```python
def solution(n):
    if n % 7 == 0:
        return n // 7
    else:
        return n // 7 + 1
```

---

## [014] 피자 나눠 먹기(2) [🔎][014]

> 머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다.  
> 피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, n명이 주문한 피자를
> **남기지 않고** 모두 같은 수의 피자 조각을 먹어야 한다면
> **최소 몇 판**을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.

```python
def solution(n):
    for i in range(min(6, n), 0, -1):
        if 6 % i == 0 and n % i == 0: return n // i
```

---

## [015] 피자 나눠 먹기(3) [🔎][015]

> 머쓱이네 피자가게는 피자를 두 조각에서 열 조각까지 원하는 조각 수로 잘라줍니다.  
> 피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때, n명의 사람이 최소 한 조각 이상 피자를 먹으려면 최소 몇 판의 피자를 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.

```python
def solution(slice, n):
    if n % slice == 0: return n // slice
    return n // slice + 1
```

---

## [016] 배열의 평균값 [🔎][016]

> 정수 배열 numbers가 매개변수로 주어집니다.  
> numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

```python
def solution(numbers):
    total = 0
    for i in numbers:
        total += i
    return total / len(numbers)
```

---

[013]: https://school.programmers.co.kr/learn/courses/30/lessons/120814
[014]: https://school.programmers.co.kr/learn/courses/30/lessons/120815
[015]: https://school.programmers.co.kr/learn/courses/30/lessons/120816
[016]: https://school.programmers.co.kr/learn/courses/30/lessons/120817
