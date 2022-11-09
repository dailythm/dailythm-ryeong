# Day 24

---

## [093] 치킨 쿠폰 [🔎][093]

> 프로그래머스 치킨은 치킨을 시켜먹으면 한 마리당 쿠폰을 한 장 발급합니다.  
> 쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고, 서비스 치킨에도 쿠폰이 발급됩니다.  
> 시켜먹은 치킨의 수 chicken이 매개변수로 주어질 때 받을 수 있는 최대 서비스 치킨의 수를 return하도록 solution 함수를 완성해주세요.

```python
def solution(chicken):
    if chicken < 10 : return 0
    return chicken // 10 + solution(chicken // 10 + chicken % 10)
```

---

## [094] 이진수 더하기 [🔎][094]

> 이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때,
> 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

```python
def solution(bin1, bin2):
    answer = []
    total, num1, num2 = 0, 1, 1

    for i in reversed(bin1):
        if i == '1':
            total += num1
        num1 *= 2
    for i in reversed(bin2):
        if i == '1':
            total += num2
        num2 *= 2

    while total > 0:
        answer.append(str(total % 2))
        total = total // 2
    answer.reverse()

    if answer == [] : return '0'
    else : return ''.join(answer)
```

---

## [095] A로 B만들기 [🔎][095]

> 문자열 before와 after가 매개변수로 주어질 때, before의 순서를 바꾸어
> after를 만들 수 있으면 1을, 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.

```python
def solution(before, after):
    if sorted(before) == sorted(after): return 1
    else : return 0
```

---

## [096] k의 개수 [🔎][096]

> 1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다.  
> 정수 i, j, k가 매개변수로 주어질 때, i부터 j까지 k가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.

```python
def solution(i, j, k):
    answer = 0
    for a in range(i, j +1):
        for b in str(a):
            if b == str(k) : answer += 1
    return answer
```

---

[093]: https://school.programmers.co.kr/learn/courses/30/lessons/120884
[094]: https://school.programmers.co.kr/learn/courses/30/lessons/120885
[095]: https://school.programmers.co.kr/learn/courses/30/lessons/120886
[096]: https://school.programmers.co.kr/learn/courses/30/lessons/120887
