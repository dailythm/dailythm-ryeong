# Day 2

---

## [005] 두 수의 나눗셈 [🔎][005]

> 정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 solution 함수를 완성해주세요.

```python
def solution(num1, num2):
    return num1 / num2 * 1000 // 1
```

---

## [006] 숫자 비교하기 [🔎][006]

> 정수 num1과 num2가 주어질 때, num1에서 num2를 뺀 값을 return하도록 solution 함수를 완성해주세요.

```python
def solution(num1, num2):
    if num1 == num2 : return 1
    else : return -1
```

---

## [007] 분수의 덧셈 [🔎][007]

> 첫 번째 분수의 분자와 분모를 뜻하는 denum1, num1, 두 번째 분수의 분자와 분모를 뜻하는 denum2, num2가 매개변수로 주어집니다.  
> 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

```python
def solution(denum1, num1, denum2, num2):
    answer = [denum1*num2 + denum2*num1, num1*num2]
    for i in range(min(answer[0],answer[1]), 0, -1):
        if answer[0] % i == 0 and answer[1] % i == 0:
            answer = [answer[0] / i, answer[1] / i]
    return answer
```

---

## [008] 배열 두 배 만들기 [🔎][008]

> 정수 배열 numbers가 매개변수로 주어집니다.  
> numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

```python
def solution(numbers):
    answer = []
    for i in numbers:
        answer.append( i * 2 )
    return answer
```

---

[005]: https://school.programmers.co.kr/learn/courses/30/lessons/120806
[006]: https://school.programmers.co.kr/learn/courses/30/lessons/120807
[007]: https://school.programmers.co.kr/learn/courses/30/lessons/120808
[008]: https://school.programmers.co.kr/learn/courses/30/lessons/120809
