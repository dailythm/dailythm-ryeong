# url : https://school.programmers.co.kr/learn/courses/30/lessons/120888


'''
문제 : 문자열 my_string이 매개변수로 주어집니다. 
      my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.

'''

def solution(my_string):
    answer = ''
    for i in my_string:
        check = True
        for j in answer:
            if i == j:
                check = False
                break
        if check : answer += i
    return answer