# Day 24

---

## [093] ์นํจ ์ฟ ํฐ [๐][093]

> ํ๋ก๊ทธ๋๋จธ์ค ์นํจ์ ์นํจ์ ์์ผ๋จน์ผ๋ฉด ํ ๋ง๋ฆฌ๋น ์ฟ ํฐ์ ํ ์ฅ ๋ฐ๊ธํฉ๋๋ค.  
> ์ฟ ํฐ์ ์ด ์ฅ ๋ชจ์ผ๋ฉด ์นํจ์ ํ ๋ง๋ฆฌ ์๋น์ค๋ก ๋ฐ์ ์ ์๊ณ , ์๋น์ค ์นํจ์๋ ์ฟ ํฐ์ด ๋ฐ๊ธ๋ฉ๋๋ค.  
> ์์ผ๋จน์ ์นํจ์ ์ chicken์ด ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋ ๋ฐ์ ์ ์๋ ์ต๋ ์๋น์ค ์นํจ์ ์๋ฅผ returnํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด์ฃผ์ธ์.

```python
def solution(chicken):
    if chicken < 10 : return 0
    return chicken // 10 + solution(chicken // 10 + chicken % 10)
```

---

## [094] ์ด์ง์ ๋ํ๊ธฐ [๐][094]

> ์ด์ง์๋ฅผ ์๋ฏธํ๋ ๋ ๊ฐ์ ๋ฌธ์์ด bin1๊ณผ bin2๊ฐ ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋,
> ๋ ์ด์ง์์ ํฉ์ returnํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด์ฃผ์ธ์.

```python
def solution(bin1, bin2):
    answer = []
    total, num1, num2 = 0, 1, 1

    for i in reversed(bin1):
        if i == '1':
            total += num1
        num1 *= 2
    for i in reversed(bin2):
        if i == '1':
            total += num2
        num2 *= 2

    while total > 0:
        answer.append(str(total % 2))
        total = total // 2
    answer.reverse()

    if answer == [] : return '0'
    else : return ''.join(answer)
```

---

## [095] A๋ก B๋ง๋ค๊ธฐ [๐][095]

> ๋ฌธ์์ด before์ after๊ฐ ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋, before์ ์์๋ฅผ ๋ฐ๊พธ์ด
> after๋ฅผ ๋ง๋ค ์ ์์ผ๋ฉด 1์, ๋ง๋ค ์ ์์ผ๋ฉด 0์ return ํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด๋ณด์ธ์.

```python
def solution(before, after):
    if sorted(before) == sorted(after): return 1
    else : return 0
```

---

## [096] k์ ๊ฐ์ [๐][096]

> 1๋ถํฐ 13๊น์ง์ ์์์, 1์ 1, 10, 11, 12, 13 ์ด๋ ๊ฒ ์ด 6๋ฒ ๋ฑ์ฅํฉ๋๋ค.  
> ์ ์ i, j, k๊ฐ ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋, i๋ถํฐ j๊น์ง k๊ฐ ๋ช ๋ฒ ๋ฑ์ฅํ๋์ง return ํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด์ฃผ์ธ์.

```python
def solution(i, j, k):
    answer = 0
    for a in range(i, j +1):
        for b in str(a):
            if b == str(k) : answer += 1
    return answer
```

---

[093]: https://school.programmers.co.kr/learn/courses/30/lessons/120884
[094]: https://school.programmers.co.kr/learn/courses/30/lessons/120885
[095]: https://school.programmers.co.kr/learn/courses/30/lessons/120886
[096]: https://school.programmers.co.kr/learn/courses/30/lessons/120887
