# Day 17

---

## [065] 숫자 찾기 [🔎][065]

> 정수 num과 k가 매개변수로 주어질 때,
> num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고
> 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

```python
def solution(num, k):
    text = str(num)
    index = text.find(str(k))
    if index == -1 : return -1
    return index +1
```

---

## [066] n의 배수 고르기 [🔎][066]

> 정수 n과 정수 배열 numlist가 매개변수로 주어질 때,
> numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.

```python
def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0 : answer.append(i)
    return answer
```

---

## [067] 자릿수 더하기 [🔎][067]

> 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요

```python
def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer
```

---

## [068] OX퀴즈 [🔎][068]

> 덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다.  
> 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.

```python
def solution(quiz):
    answer = []

    for i in quiz:
        arr = i.split(' ')
        if arr[1] =='-' : curr = int(arr[0]) - int(arr[2])
        else : curr = int(arr[0]) + int(arr[2])

        if str(curr) == arr[4]: answer.append("O")
        else : answer.append("X")

    return answer
```

---

[065]: https://school.programmers.co.kr/learn/courses/30/lessons/120904
[066]: https://school.programmers.co.kr/learn/courses/30/lessons/120905
[067]: https://school.programmers.co.kr/learn/courses/30/lessons/120906
[068]: https://school.programmers.co.kr/learn/courses/30/lessons/120907
