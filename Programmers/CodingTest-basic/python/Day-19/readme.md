# Day 19

---

## [073] 7์ ๊ฐ์ [๐][073]

> ๋จธ์ฑ์ด๋ ํ์ด์ ์ซ์ 7์ ๊ฐ์ฅ ์ข์ํฉ๋๋ค.  
> ์ ์ ๋ฐฐ์ด array๊ฐ ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋, 7์ด ์ด ๋ช ๊ฐ ์๋์ง return ํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด๋ณด์ธ์.

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

## [074] ์๋ผ์ ๋ฐฐ์ด๋ก ์ ์ฅํ๊ธฐ [๐][074]

> ๋ฌธ์์ด my_str๊ณผ n์ด ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋, my_str์ ๊ธธ์ด n์ฉ ์๋ผ์ ์ ์ฅํ ๋ฐฐ์ด์ returnํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด์ฃผ์ธ์.

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

## [075] ์ค๋ณต๋ ์ซ์ ๊ฐ์ [๐][075]

> ์ ์๊ฐ ๋ด๊ธด ๋ฐฐ์ด array์ ์ ์ n์ด ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋, array์ n์ด ๋ช ๊ฐ ์๋ ์ง๋ฅผ return ํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด๋ณด์ธ์.

```python
def solution(array, n):
    answer = 0
    for i in array:
        if i == n : answer += 1
    return answer
```

---

## [076] ๋จธ์ฑ์ด๋ณด๋ค ํค ํฐ ์ฌ๋ [๐][076]

> ๋จธ์ฑ์ด๋ ํ๊ต์์ ํค ์์ผ๋ก ์ค์ ์ค ๋ ๋ช ๋ฒ์งธ๋ก ์์ผ ํ๋์ง ๊ถ๊ธํด์ก์ต๋๋ค.  
> ๋จธ์ฑ์ด๋ค ๋ฐ ์น๊ตฌ๋ค์ ํค๊ฐ ๋ด๊ธด ์ ์ ๋ฐฐ์ด array์ ๋จธ์ฑ์ด์ ํค height๊ฐ ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋,
> ๋จธ์ฑ์ด๋ณด๋ค ํค ํฐ ์ฌ๋ ์๋ฅผ return ํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด๋ณด์ธ์.

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
