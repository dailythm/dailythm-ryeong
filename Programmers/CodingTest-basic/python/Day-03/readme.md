# Day 3

---

## [009] 나머지 구하기 [🔎][009]

> 정수 num1, num2가 매개변수로 주어질 때, num1를 num2로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.

```python
def solution(num1, num2):
    return num1 % num2
```

---

## [010] 중앙값 구하기 [🔎][010]

> 중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다.  
> 정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.

```python
def solution(array):
    array.sort()
    return array[len(array)//2]
```

---

## [011] 최빈값 구하기 [🔎][011]

> 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다.  
> 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요.  
> 최빈값이 여러 개면 -1을 return 합니다.

```python
def solution(array):
    max = [0,0]
    for i in set(array):
        count = array.count(i)
        if(count > max[0]):
            max[0] = count
            max[1] = i
        elif(count == max[0]):
            max[1] = -1
    return max[1]
```

---

## [012] 짝수는 싫어요 [🔎][012]

> 정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.

```python
def solution(n):
    answer = []
    for i in range(1, n+1, 2):
        answer.append(i)
    return answer
```

---

[009]: https://school.programmers.co.kr/learn/courses/30/lessons/120810
[010]: https://school.programmers.co.kr/learn/courses/30/lessons/120811
[011]: https://school.programmers.co.kr/learn/courses/30/lessons/120812
[012]: https://school.programmers.co.kr/learn/courses/30/lessons/120813
