# Day 8

---

## [029] 배열 자르기 [🔎][029]

> 정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때, numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성해보세요.

```python
def solution(numbers, num1, num2):
    return numbers[num1 : num2 + 1]
```

---

## [030] 외계행성의 나이 [🔎][030]

> 우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다.  
> 입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다.  
> a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다.  
> 나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.

```python
def solution(age):
    alphabet = ['a','b','c','d','e','f','g','h','i','j']
    answer = ''
    for i in str(age):
        answer += alphabet[int(i)]
    return answer
```

---

## [031] 진료순서 정하기 [🔎][031]

> 외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다.  
> 정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.

```python
def solution(emergency):
    answer = [0 for i in range(len(emergency))]
    for i in range(len(emergency)):
        for j in range(len(emergency)):
            if emergency[i] <= emergency[j]:
                answer[i] += 1
    return answer
```

---

## [032] 순서쌍의 개수 [🔎][032]

> 순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다.  
> 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.

```python
def solution(n):
    answer = 0
    sqrt = int (n ** (1/2) // 1)
    for i in range(1, sqrt + 1):
        if n % i == 0 :
            answer += 2
    if n % n ** (1/2) == 0 :
        answer -= 1
    return answer
```

---

[029]: https://school.programmers.co.kr/learn/courses/30/lessons/120833
[030]: https://school.programmers.co.kr/learn/courses/30/lessons/120834
[031]: https://school.programmers.co.kr/learn/courses/30/lessons/120835
[032]: https://school.programmers.co.kr/learn/courses/30/lessons/120836
