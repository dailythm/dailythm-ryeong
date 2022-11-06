# Day 16

---

## [061] 편지 [🔎][061]

> 머쓱이는 할머니께 생신 축하 편지를 쓰려고 합니다.  
> 할머니가 보시기 편하도록 글자 한 자 한 자를 가로 2cm 크기로 적으려고 하며, 편지를 가로로만 적을 때,
> 축하 문구 message를 적기 위해 필요한 편지지의 최소 가로길이를 return 하도록 solution 함수를 완성해주세요.

```python
def solution(message):
    return len(message) * 2
```

---

## [062] 가장 큰 수 찾기 [🔎][062]

> 정수 배열 array가 매개변수로 주어질 때,
> 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

```python
def solution(array):
    big = 0
    for i in array:
        if big < i : big = i
    return [big, array.index(big)]
```

---

## [063] 문자열 계산하기 [🔎][063]

> my_string은 "3 + 5"처럼 문자열로 된 수식입니다.  
> 문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.

```python
def solution(my_string):
    arr = my_string.split(' ')
    answer = int(arr[0])
    for i in range(1, len(arr), 2):
        if arr[i] == '+' : answer += int(arr[i+1])
        else : answer -= int(arr[i+1])
    return answer
```

---

## [064] 배열의 유사도 [🔎][064]

> 두 배열이 얼마나 유사한지 확인해보려고 합니다.  
> 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

```python
def solution(s1, s2):
    return len(s1) + len(s2) - len(set(s1+s2))
```

---

[061]: https://school.programmers.co.kr/learn/courses/30/lessons/120898
[062]: https://school.programmers.co.kr/learn/courses/30/lessons/120899
[063]: https://school.programmers.co.kr/learn/courses/30/lessons/120902
[064]: https://school.programmers.co.kr/learn/courses/30/lessons/120903
