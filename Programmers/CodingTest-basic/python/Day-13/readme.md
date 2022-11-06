# Day 13

---

## [049] 컨트롤 제트 [🔎][049]

> 숫자들이 공백으로 구분된 문자열이 주어집니다.
> 문자열에 있는 숫자를 차례대로 더하려고 합니다.  
> 이 때 “Z”가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다.  
> 숫자와 “Z”로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.

```python
def solution(s):
    answer = 0
    arr = []
    for i in s.split(' '):
        if i == 'Z' and len(arr) > 0 : arr.pop()
        else : arr.append(i)
    for i in arr:
        answer += int(i)
    return answer
```

---

## [050] 배열 원소의 길이 [🔎][050]

> 문자열 배열 strlist가 매개변수로 주어집니다.  
> strlist 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.

```python
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer
```

---

## [051] 중복된 문자 제거 [🔎][051]

> 문자열 my_string이 매개변수로 주어집니다.  
> my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.

```python
def solution(my_string):
    answer = ''
    for i in my_string:
        check = True
        for j in answer:
            if i == j:
                check = False
                break
        if check : answer += i
    return answer
```

---

## [052] 삼각형의 완성조건 [🔎][052]

> 선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

- 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.

> 삼각형의 세 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다.  
> 세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return하도록 solution 함수를 완성해주세요.

```python
def solution(sides):
    long, total= 0, 0
    for i in sides:
        total += i
        if i > long : long = i
    if long < total - long : return 1
    else : return 2
```

---

[049]: https://school.programmers.co.kr/learn/courses/30/lessons/120853
[050]: https://school.programmers.co.kr/learn/courses/30/lessons/120854
[051]: https://school.programmers.co.kr/learn/courses/30/lessons/120888
[052]: https://school.programmers.co.kr/learn/courses/30/lessons/120889
