# Day 18

---

## [069] 문자열안에 문자열 [🔎][069]

> 문자열 str1, str2가 매개변수로 주어집니다.  
> str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.

```python
def solution(str1, str2):
    if str1.find(str2) == -1: return 2
    else: return 1
```

---

## [070] 제곱수 판별하기 [🔎][070]

> 어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다.
> 정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.

```python
def solution(n):
    if n ** (1/2) % 1 == 0 : return 1
    else : return 2
```

---

## [071] 세균 증식 [🔎][071]

> 어떤 세균은 1시간에 두배만큼 증식한다고 합니다.  
> 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때
> t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.

```python
def solution(n, t):
    return n * (2 ** t)
```

---

## [072] 문자열 정렬하기(2) [🔎][072]

> 영어 대소문자로 이루어진 문자열 my_string이 매개변수로 주어질 때,
> my_string을 모두 소문자로 바꾸고 알파벳 순서대로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.

```python
def solution(my_string):
    return ''.join(sorted(my_string.lower()))
```

---

[069]: https://school.programmers.co.kr/learn/courses/30/lessons/120908
[070]: https://school.programmers.co.kr/learn/courses/30/lessons/120909
[071]: https://school.programmers.co.kr/learn/courses/30/lessons/120910
[072]: https://school.programmers.co.kr/learn/courses/30/lessons/120911
