# Day 17

---

## [065] ์ซ์ ์ฐพ๊ธฐ [๐][065]

> ์ ์ num๊ณผ k๊ฐ ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋,
> num์ ์ด๋ฃจ๋ ์ซ์ ์ค์ k๊ฐ ์์ผ๋ฉด num์ ๊ทธ ์ซ์๊ฐ ์๋ ์๋ฆฌ ์๋ฅผ returnํ๊ณ 
> ์์ผ๋ฉด -1์ return ํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด๋ณด์ธ์.

```python
def solution(num, k):
    text = str(num)
    index = text.find(str(k))
    if index == -1 : return -1
    return index +1
```

---

## [066] n์ ๋ฐฐ์ ๊ณ ๋ฅด๊ธฐ [๐][066]

> ์ ์ n๊ณผ ์ ์ ๋ฐฐ์ด numlist๊ฐ ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋,
> numlist์์ n์ ๋ฐฐ์๊ฐ ์๋ ์๋ค์ ์ ๊ฑฐํ ๋ฐฐ์ด์ returnํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด์ฃผ์ธ์.

```python
def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0 : answer.append(i)
    return answer
```

---

## [067] ์๋ฆฟ์ ๋ํ๊ธฐ [๐][067]

> ์ ์ n์ด ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋ n์ ๊ฐ ์๋ฆฌ ์ซ์์ ํฉ์ returnํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด์ฃผ์ธ์

```python
def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer
```

---

## [068] OXํด์ฆ [๐][068]

> ๋ง์, ๋บ์ ์์๋ค์ด 'X [์ฐ์ฐ์] Y = Z' ํํ๋ก ๋ค์ด์๋ ๋ฌธ์์ด ๋ฐฐ์ด quiz๊ฐ ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง๋๋ค.  
> ์์์ด ์ณ๋ค๋ฉด "O"๋ฅผ ํ๋ฆฌ๋ค๋ฉด "X"๋ฅผ ์์๋๋ก ๋ด์ ๋ฐฐ์ด์ returnํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด์ฃผ์ธ์.

```python
def solution(quiz):
    answer = []

    for i in quiz:
        arr = i.split(' ')
        if arr[1] =='-' : curr = int(arr[0]) - int(arr[2])
        else : curr = int(arr[0]) + int(arr[2])

        if str(curr) == arr[4]: answer.append("O")
        else : answer.append("X")

    return answer
```

---

[065]: https://school.programmers.co.kr/learn/courses/30/lessons/120904
[066]: https://school.programmers.co.kr/learn/courses/30/lessons/120905
[067]: https://school.programmers.co.kr/learn/courses/30/lessons/120906
[068]: https://school.programmers.co.kr/learn/courses/30/lessons/120907
