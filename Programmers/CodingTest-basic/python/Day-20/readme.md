# Day 20

---

## [077] 직사각형 넓이 구하기 [🔎][077]

> 2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다.  
> 직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는 배열 dots가 매개변수로 주어질 때,
> 직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요.

```python
def solution(dots):
    width, length = 0, 0
    for i in dots:
        width += i[0]
        length += i[1]
    width = abs(width / 4 - dots[0][0]) * 2
    length = abs(length / 4 - dots[0][1]) * 2
    return int(width * length)
```

---

## [078] 캐릭터의 좌표 [🔎][078]

> 머쓱이는 RPG게임을 하고 있습니다.  
> 게임에는 up, down, left, right 방향키가 있으며 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다.  
> 예를 들어 [0,0]에서 up을 누른다면 캐릭터의 좌표는 [0, 1], down을 누른다면 [0, -1],
> left를 누른다면 [-1, 0], right를 누른다면 [1, 0]입니다.  
> 머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다.  
> 캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 캐릭터의 좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.
>
> - [0, 0]은 board의 정 중앙에 위치합니다.  
>   예를 들어 board의 가로 크기가 9라면 캐릭터는 왼쪽으로 최대 [-4, 0]까지 오른쪽으로 최대 [4, 0]까지 이동할 수 있습니다.

```python
def solution(keyinput, board):
    answer = [0, 0]
    row, col = board[0]//2, board[1]//2
    for i in keyinput:
        if i == "right" and not answer[0] == row: answer[0] += 1
        elif i == 'left' and not answer[0] == -row : answer[0] -= 1
        elif i == "up" and not answer[1] == col : answer[1] += 1
        elif i == 'down' and not answer[1] == -col : answer[1] -= 1
    return answer
```

---

## [079] 최댓값 만들기 [🔎][079]

> 정수 배열 numbers가 매개변수로 주어집니다.  
> numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

```python
def solution(numbers):
    sort = sorted(numbers)
    if sort[0] * sort[1] > sort[-1] * sort[-2]:
        return sort[0] * sort[1]
    else : return sort[-1] * sort[-2]
```

---

## [080] 다항식 더하기 [🔎][080]

> 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다.  
> 다항식을 계산할 때는 동류항끼리 계산해 정리합니다.  
> 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요.  
> 같은 식이라면 가장 짧은 수식을 return 합니다.

```python
def solution(polynomial):
    answer = []
    linear, const = 0, 0

    for i in polynomial.split(' + '):
        if i.isdigit() : const += int(i)
        elif i == 'x' : linear += 1
        else : linear += int(i[:-1])

    if linear == 1 : answer.append('x')
    elif linear > 1 : answer.append(str(linear) + 'x')
    if const > 0 : answer.append(str(const))

    return ' + '.join(answer)
```

---

[077]: https://school.programmers.co.kr/learn/courses/30/lessons/120860
[078]: https://school.programmers.co.kr/learn/courses/30/lessons/120861
[079]: https://school.programmers.co.kr/learn/courses/30/lessons/120862
[080]: https://school.programmers.co.kr/learn/courses/30/lessons/120863
