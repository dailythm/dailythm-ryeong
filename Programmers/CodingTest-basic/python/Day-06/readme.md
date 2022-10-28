# Day 6

---

## [021] 문자열 뒤집기 [🔎][021]

> 문자열 my_string이 매개변수로 주어집니다.  
> my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.

```python
def solution(my_string):
    answer = ''
    for i in my_string:
        answer = i + answer
    return answer
```

---

## [022] 직각삼각형 출력하기 [🔎][022]

> "_"의 높이와 너비를 1이라고 했을 때, "_"을 이용해 직각 이등변 삼각형을 그리려고합니다.  
> 정수 n 이 주어지면 높이와 너비가 n 인 직각 이등변 삼각형을 출력하도록 코드를 작성해보세요.

```python
n = int(input())
for i in range(1, n + 1, 1):
    print('*' * i)
```

---

## [023] 짝수 홀수 개수 [🔎][023]

> 정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

```python
def solution(num_list):
    answer = [0, 0]
    for i in num_list:
        if i % 2 == 0:
            answer[0] = answer[0] + 1
        else:
            answer[1] = answer[1] + 1
    return answer
```

---

## [024] 문자 반복 출력하기 [🔎][024]

> 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.

```python
def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i * n
    return answer
```

---

[021]: https://school.programmers.co.kr/learn/courses/30/lessons/120822
[022]: https://school.programmers.co.kr/learn/courses/30/lessons/120823
[023]: https://school.programmers.co.kr/learn/courses/30/lessons/120824
[024]: https://school.programmers.co.kr/learn/courses/30/lessons/120825
