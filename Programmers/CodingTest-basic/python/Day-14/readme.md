# Day 14

---

## [053] ๊ฐ๊น์ด ์ [๐][053]

> ์ ์ ๋ฐฐ์ด array์ ์ ์ n์ด ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋,
> array์ ๋ค์ด์๋ ์ ์ ์ค n๊ณผ ๊ฐ์ฅ ๊ฐ๊น์ด ์๋ฅผ return ํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด์ฃผ์ธ์.

```python
def solution(array, n):
    answer = 0
    maxDiff = 100
    array = sorted(array)
    for i in array:
        diff = int(((n - i) ** 2) ** (1/2))
        if diff < maxDiff:
            maxDiff = diff
            answer = i
    return answer
```

---

## [054] 369๊ฒ์ [๐][054]

> ๋จธ์ฑ์ด๋ ์น๊ตฌ๋ค๊ณผ 369๊ฒ์์ ํ๊ณ  ์์ต๋๋ค.  
> 369๊ฒ์์ 1๋ถํฐ ์ซ์๋ฅผ ํ๋์ฉ ๋๋ฉฐ 3, 6, 9๊ฐ ๋ค์ด๊ฐ๋ ์ซ์๋ ์ซ์ ๋์  3, 6, 9์ ๊ฐ์๋งํผ ๋ฐ์๋ฅผ ์น๋ ๊ฒ์์๋๋ค.  
> ๋จธ์ฑ์ด๊ฐ ๋งํด์ผํ๋ ์ซ์ order๊ฐ ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋,
> ๋จธ์ฑ์ด๊ฐ ์ณ์ผํ  ๋ฐ์ ํ์๋ฅผ return ํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด๋ณด์ธ์.

```python
def solution(order):
    answer = 0
    for i in str(order):
        if i == '3' or i == '6' or i == '9':
            answer += 1
    return answer
```

---

## [055] ์ํธ ํด๋ [๐][055]

> ๊ตฐ ์ ๋ต๊ฐ ๋จธ์ฑ์ด๋ ์ ์ ์ค ์ ๊ตฐ์ด ๋ค์๊ณผ ๊ฐ์ ์ํธ ์ฒด๊ณ๋ฅผ ์ฌ์ฉํ๋ค๋ ๊ฒ์ ์์๋์ต๋๋ค.

- ์ํธํ๋ ๋ฌธ์์ด cipher๋ฅผ ์ฃผ๊ณ ๋ฐ์ต๋๋ค.
- ๊ทธ ๋ฌธ์์ด์์ code์ ๋ฐฐ์ ๋ฒ์งธ ๊ธ์๋ง ์ง์ง ์ํธ์๋๋ค.

> ๋ฌธ์์ด cipher์ ์ ์ code๊ฐ ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋ ํด๋๋ ์ํธ ๋ฌธ์์ด์ returnํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด์ฃผ์ธ์.

```python
def solution(cipher, code):
    answer = ''
    for i in range(code -1, len(cipher), code):
        answer += cipher[i]
    return answer
```

---

## [056] ๋๋ฌธ์์ ์๋ฌธ์ [๐][056]

> ๋ฌธ์์ด my_string์ด ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋,
> ๋๋ฌธ์๋ ์๋ฌธ์๋ก ์๋ฌธ์๋ ๋๋ฌธ์๋ก ๋ณํํ ๋ฌธ์์ด์ returnํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด์ฃผ์ธ์.

```python
def solution(my_string):
    return my_string.swapcase()
```

---

[053]: https://school.programmers.co.kr/learn/courses/30/lessons/120890
[054]: https://school.programmers.co.kr/learn/courses/30/lessons/120891
[055]: https://school.programmers.co.kr/learn/courses/30/lessons/120892
[056]: https://school.programmers.co.kr/learn/courses/30/lessons/120893
