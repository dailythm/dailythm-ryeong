# Day 12

---

## [045] ๋ชจ์ ์ ๊ฑฐ [๐][045]

> ์์ด์์  a, e, i, o, u ๋ค์ฏ ๊ฐ์ง ์ํ๋ฒณ์ ๋ชจ์์ผ๋ก ๋ถ๋ฅํฉ๋๋ค.  
> ๋ฌธ์์ด my_string์ด ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋ ๋ชจ์์ ์ ๊ฑฐํ ๋ฌธ์์ด์ returnํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด์ฃผ์ธ์.

```python
def solution(my_string):
    answer = ''
    for i in my_string:
        if not (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            answer += i
    return answer
```

---

## [046] ๋ฌธ์์ด ์ ๋ ฌํ๊ธฐ(1) [๐][046]

> ๋ฌธ์์ด my_string์ด ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋, my_string ์์ ์๋ ์ซ์๋ง ๊ณจ๋ผ ์ค๋ฆ์ฐจ์ ์ ๋ ฌํ ๋ฆฌ์คํธ๋ฅผ return ํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด๋ณด์ธ์.

```python
def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit() : answer.append(int(i))
    return sorted(answer)
```

---

## [047] ์จ์ด์๋ ์ซ์์ ๋ง์ [๐][047]

> ๋ฌธ์์ด my_string์ด ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง๋๋ค.  
> my_string์์ ๋ชจ๋  ์์ฐ์๋ค์ ํฉ์ returnํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด์ฃผ์ธ์.

```python
def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit() : answer += int(i)
    return answer
```

---

## [048] ์์ธ์๋ถํด [๐][048]

> ์์ธ์๋ถํด๋ ์ด๋ค ์๋ฅผ ์์๋ค์ ๊ณฑ์ผ๋ก ํํํ๋ ๊ฒ์๋๋ค.  
> ์๋ฅผ ๋ค์ด 12๋ฅผ ์์ธ์ ๋ถํดํ๋ฉด 2 _ 2 _ 3 ์ผ๋ก ๋ํ๋ผ ์ ์์ต๋๋ค.
> ๋ฐ๋ผ์ 12์ ์์ธ์๋ 2์ 3์๋๋ค.  
> ์์ฐ์ n์ด ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง ๋ n์ ์์ธ์๋ฅผ ์ค๋ฆ์ฐจ์์ผ๋ก ๋ด์ ๋ฐฐ์ด์ returnํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด์ฃผ์ธ์.

```python
def solution(n):
    answer = []
    for i in range(2, int(n // 2) +1):
        if n % i == 0: answer.append(i)
        while n % i == 0:
            n /= i
    if answer == [] : return [n]
    else : return answer
```

---

[045]: https://school.programmers.co.kr/learn/courses/30/lessons/120849
[046]: https://school.programmers.co.kr/learn/courses/30/lessons/120850
[047]: https://school.programmers.co.kr/learn/courses/30/lessons/120851
[048]: https://school.programmers.co.kr/learn/courses/30/lessons/120852
