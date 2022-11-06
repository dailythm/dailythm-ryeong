# Day 15

---

## [057] 영어가 싫어요 [🔎][057]

> 영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다.  
> 문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.

```python
def solution(numbers):
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(10):
        numbers = numbers.replace(num[i], str(i))
    return int(numbers)
```

---

## [058] 인덱스 바꾸기 [🔎][058]

> 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때,
> my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.

```python
def solution(txt, num1, num2):
    if num1 > num2 : big, small = num1, num2
    else : big, small = num2, num1
    return txt[:small] + txt[big] + txt[small+1:big] + txt[small] + txt[big+1:]
```

---

## [059] 한 번만 등장한 문자 [🔎][059]

> 문자열 s가 매개변수로 주어집니다.  
> s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.  
> 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.

```python
def solution(s):
    answer = []
    for i in set(list(s)):
        if s.count(i) == 1 : answer.append(i)
    return ''.join(sorted(answer))
```

---

## [060] 약수 구하기 [🔎][060]

> 정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

```python
def solution(n):
    answer = []
    sqrt = n ** (1/2)
    for i in range(1, int(sqrt) +1):
        if n % i == 0 : answer += [n // i, i]
    return sorted(list(set(answer)))
```

---

[057]: https://school.programmers.co.kr/learn/courses/30/lessons/120894
[058]: https://school.programmers.co.kr/learn/courses/30/lessons/120895
[059]: https://school.programmers.co.kr/learn/courses/30/lessons/120896
[060]: https://school.programmers.co.kr/learn/courses/30/lessons/120897
