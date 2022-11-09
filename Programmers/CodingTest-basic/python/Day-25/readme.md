# Day 25

---

## [097] 문자열 밀기 [🔎][097]

> 문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다.  
> 이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때,
> A를 밀어서 B가 될 수 있다면 몇 번 밀어야 하는지 횟수를 return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

```python
def solution(A, B):
    A = list(A)
    for i in range(len(B)) :
        if ''.join(A) == B : return i
        front = A.pop()
        A = [front] + A
    return -1
```

---

## [098] 종이 자르기 [🔎][098]

> 머쓱이는 큰 종이를 1 x 1 크기로 자르려고 합니다.  
> 예를 들어 2 x 2 크기의 종이를 1 x 1 크기로 자르려면 최소 가위질 세 번이 필요합니다.  
> 정수 M, N이 매개변수로 주어질 때, M x N 크기의 종이를 최소로 가위질 해야하는 횟수를 return 하도록 solution 함수를 완성해보세요.

```python
def solution(M, N):
    if N > M : N, M = M, N
    return N-1 + (M-1) *N
```

---

## [099] 연속된 수의 합 [🔎][099]

> 연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 두 정수 num과 total이 주어집니다.  
> 연속된 수 num개를 더한 값이 total이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.

```python
def solution(num, total):
    answer = []
    for i in range(1, num):
        total -= i
    start = total // num
    for i in range(start, start + num):
        answer.append(i)
    return answer
```

---

## [100] 다음에 올 숫자 [🔎][100]

> 등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.

```python
def solution(common):
    n1, n2 = common[1] - common[0], common[2] - common[1]
    if n1 == n2 : return common[-1] + n1
    else: return common[-1] * common[1] / common[0]
```

---

[097]: https://school.programmers.co.kr/learn/courses/30/lessons/120921
[098]: https://school.programmers.co.kr/learn/courses/30/lessons/120922
[099]: https://school.programmers.co.kr/learn/courses/30/lessons/120923
[100]: https://school.programmers.co.kr/learn/courses/30/lessons/120924
