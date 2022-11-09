# Day 21

---

## [081] 숨어있는 숫자의 덧셈(2) [🔎][081]

> 문자열 my_string이 매개변수로 주어집니다.  
> my_string은 소문자, 대문자, 자연수로만 구성되어있습니다.  
> my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

```python
def solution(my_string):
    answer = 0
    arr = []
    check = False
    for i in my_string :
        if i.isdigit() and check :
            arr[-1] += i
        elif i.isdigit() :
            arr.append(i)
            check = True
        else : check = False
    for i in arr : answer += int(i)
    return answer
```

---

## [082] 안전지대 [🔎][082]

> 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.  
> 지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.  
> 지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

```python
def solution(board):
    answer = 0
    leng = len(board)
    danger = [[0 for i in range(leng+2)] for i in range(leng+2)]
    for i in range(leng):
        for j in range(leng):
            if board[i][j] == 1:
                danger[i][j], danger[i][j+1], danger[i][j+2] = 1, 1, 1
                danger[i+1][j], danger[i+1][j+1], danger[i+1][j+2] = 1, 1, 1
                danger[i+2][j], danger[i+2][j+1], danger[i+2][j+2] = 1, 1, 1
    for i in range(1, leng+1):
        for j in range(1, leng+1):
            if danger[i][j] == 0 : answer += 1
    return answer
```

---

## [083] 삼각형의 완성조건(2) [🔎][083]

> 선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

- 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.  
  삼각형의 두 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다.

> 나머지 한 변이 될 수 있는 정수의 개수를 return하도록 solution 함수를 완성해주세요.

```python
def solution(sides):
    answer = 0
    if sides[0] > sides[1] : big, small = sides[0], sides[1]
    else : big, small = sides[1], sides[0]

    for i in range(big - small +1, big +1): answer += 1
    for i in range(big +1, sides[0] + sides[1]): answer += 1
    return answer
```

---

## [084] 외계어 사전 [🔎][084]

> PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다.  
> 알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다.  
> spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.

```python
def solution(spell, dic):
    for i in dic:
        i = set(list(i))
        if not len(i) == len(spell): continue

        check = True
        for j in i:
            if not j in spell : check = False
        if check : return 1
    return 2
```

---

[081]: https://school.programmers.co.kr/learn/courses/30/lessons/120864
[082]: https://school.programmers.co.kr/learn/courses/30/lessons/120866
[083]: https://school.programmers.co.kr/learn/courses/30/lessons/120868
[084]: https://school.programmers.co.kr/learn/courses/30/lessons/120869
