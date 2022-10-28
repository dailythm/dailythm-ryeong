# Day 5

---

## [017] 옷가게 할인 받기 [🔎][017]

> 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.  
> 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.

```python
def solution(price):
    if(price < 100000):
        return price
    elif(price < 300000):
        return price * 0.95 // 1
    elif(price < 500000):
        return price * 0.9 // 1
    return price * 0.8 // 1
```

---

## [018] 아이스 아메리카노 [🔎][018]

> 머쓱이는 추운 날에도 아이스 아메리카노만 마십니다.  
> 아이스 아메리카노는 한잔에 5,500원입니다.  
> 머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때, 머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

```python
def solution(money):
    return [money // 5500, money % 5500]
```

---

## [019] 나이 출력 [🔎][019]

> 머쓱이는 40살인 선생님이 몇 년도에 태어났는지 궁금해졌습니다.  
> 나이 age가 주어질 때, 2022년을 기준 출생 연도를 return 하는 solution 함수를 완성해주세요.

```python
def solution(num_list):
    answer = []
    length = len(num_list)
    for i in range(0, length, 1):
        answer.append(num_list.pop())
    return answer
```

---

## [020] 배열 뒤집기 [🔎][020]

> 정수 배열 numbers가 매개변수로 주어집니다.  
> numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

```python
def solution(num_list):
    answer = []
    length = len(num_list)
    for i in range(0, length, 1):
        answer.append(num_list.pop())
    return answer
```

---

[017]: https://school.programmers.co.kr/learn/courses/30/lessons/120818
[018]: https://school.programmers.co.kr/learn/courses/30/lessons/120819
[019]: https://school.programmers.co.kr/learn/courses/30/lessons/120820
[020]: https://school.programmers.co.kr/learn/courses/30/lessons/120821
