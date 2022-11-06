# Day 14

---

## [053] 가까운 수 [🔎][053]

> 정수 배열 array와 정수 n이 매개변수로 주어질 때,
> array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.

```python
def solution(array, n):
    answer = 0
    maxDiff = 100
    array = sorted(array)
    for i in array:
        diff = int(((n - i) ** 2) ** (1/2))
        if diff < maxDiff:
            maxDiff = diff
            answer = i
    return answer
```

---

## [054] 369게임 [🔎][054]

> 머쓱이는 친구들과 369게임을 하고 있습니다.  
> 369게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 숫자는 숫자 대신 3, 6, 9의 개수만큼 박수를 치는 게임입니다.  
> 머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때,
> 머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.

```python
def solution(order):
    answer = 0
    for i in str(order):
        if i == '3' or i == '6' or i == '9':
            answer += 1
    return answer
```

---

## [055] 암호 해독 [🔎][055]

> 군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 사용한다는 것을 알아냈습니다.

- 암호화된 문자열 cipher를 주고받습니다.
- 그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.

> 문자열 cipher와 정수 code가 매개변수로 주어질 때 해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.

```python
def solution(cipher, code):
    answer = ''
    for i in range(code -1, len(cipher), code):
        answer += cipher[i]
    return answer
```

---

## [056] 대문자와 소문자 [🔎][056]

> 문자열 my_string이 매개변수로 주어질 때,
> 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.

```python
def solution(my_string):
    return my_string.swapcase()
```

---

[053]: https://school.programmers.co.kr/learn/courses/30/lessons/120890
[054]: https://school.programmers.co.kr/learn/courses/30/lessons/120891
[055]: https://school.programmers.co.kr/learn/courses/30/lessons/120892
[056]: https://school.programmers.co.kr/learn/courses/30/lessons/120893
