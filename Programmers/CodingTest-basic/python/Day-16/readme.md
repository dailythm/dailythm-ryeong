# Day 16

---

## [061] ํธ์ง [๐][061]

> ๋จธ์ฑ์ด๋ ํ ๋จธ๋๊ป ์์  ์ถํ ํธ์ง๋ฅผ ์ฐ๋ ค๊ณ  ํฉ๋๋ค.  
> ํ ๋จธ๋๊ฐ ๋ณด์๊ธฐ ํธํ๋๋ก ๊ธ์ ํ ์ ํ ์๋ฅผ ๊ฐ๋ก 2cm ํฌ๊ธฐ๋ก ์ ์ผ๋ ค๊ณ  ํ๋ฉฐ, ํธ์ง๋ฅผ ๊ฐ๋ก๋ก๋ง ์ ์ ๋,
> ์ถํ ๋ฌธ๊ตฌ message๋ฅผ ์ ๊ธฐ ์ํด ํ์ํ ํธ์ง์ง์ ์ต์ ๊ฐ๋ก๊ธธ์ด๋ฅผ return ํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด์ฃผ์ธ์.

```python
def solution(message):
    return len(message) * 2
```

---

## [062] ๊ฐ์ฅ ํฐ ์ ์ฐพ๊ธฐ [๐][062]

> ์ ์ ๋ฐฐ์ด array๊ฐ ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋,
> ๊ฐ์ฅ ํฐ ์์ ๊ทธ ์์ ์ธ๋ฑ์ค๋ฅผ ๋ด์ ๋ฐฐ์ด์ return ํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด๋ณด์ธ์.

```python
def solution(array):
    big = 0
    for i in array:
        if big < i : big = i
    return [big, array.index(big)]
```

---

## [063] ๋ฌธ์์ด ๊ณ์ฐํ๊ธฐ [๐][063]

> my_string์ "3 + 5"์ฒ๋ผ ๋ฌธ์์ด๋ก ๋ ์์์๋๋ค.  
> ๋ฌธ์์ด my_string์ด ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋, ์์์ ๊ณ์ฐํ ๊ฐ์ return ํ๋ solution ํจ์๋ฅผ ์์ฑํด์ฃผ์ธ์.

```python
def solution(my_string):
    arr = my_string.split(' ')
    answer = int(arr[0])
    for i in range(1, len(arr), 2):
        if arr[i] == '+' : answer += int(arr[i+1])
        else : answer -= int(arr[i+1])
    return answer
```

---

## [064] ๋ฐฐ์ด์ ์ ์ฌ๋ [๐][064]

> ๋ ๋ฐฐ์ด์ด ์ผ๋ง๋ ์ ์ฌํ์ง ํ์ธํด๋ณด๋ ค๊ณ  ํฉ๋๋ค.  
> ๋ฌธ์์ด ๋ฐฐ์ด s1๊ณผ s2๊ฐ ์ฃผ์ด์ง ๋ ๊ฐ์ ์์์ ๊ฐ์๋ฅผ returnํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด์ฃผ์ธ์.

```python
def solution(s1, s2):
    return len(s1) + len(s2) - len(set(s1+s2))
```

---

[061]: https://school.programmers.co.kr/learn/courses/30/lessons/120898
[062]: https://school.programmers.co.kr/learn/courses/30/lessons/120899
[063]: https://school.programmers.co.kr/learn/courses/30/lessons/120902
[064]: https://school.programmers.co.kr/learn/courses/30/lessons/120903
