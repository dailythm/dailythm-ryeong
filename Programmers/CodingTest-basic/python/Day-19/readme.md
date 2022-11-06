# Day 19

---

## [073] 7의 개수 [🔎][073]

> 머쓱이는 행운의 숫자 7을 가장 좋아합니다.  
> 정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.

```python
def solution(array):
    answer = 0
    for i in array:
        text = str(i)
        for j in text:
            if j == '7' : answer += 1
    return answer
```

---

## [074] 잘라서 배열로 저장하기 [🔎][074]

> 문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

```python
def solution(my_str, n):
    answer = []
    while len(my_str) > n :
        answer.append(my_str[0:n])
        my_str = my_str[n:]
    answer.append(my_str)
    return answer
```

---

## [075] 중복된 숫자 개수 [🔎][075]

> 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.

```python
def solution(array, n):
    answer = 0
    for i in array:
        if i == n : answer += 1
    return answer
```

---

## [076] 머쓱이보다 키 큰 사람 [🔎][076]

> 머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다.  
> 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때,
> 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.

```python
def solution(array, height):
    answer = 0
    for i in array:
        if i > height: answer +=1
    return answer
```

---

[073]: https://school.programmers.co.kr/learn/courses/30/lessons/120912
[074]: https://school.programmers.co.kr/learn/courses/30/lessons/120913
[075]: https://school.programmers.co.kr/learn/courses/30/lessons/120583
[076]: https://school.programmers.co.kr/learn/courses/30/lessons/120585
