# url : https://school.programmers.co.kr/learn/courses/30/lessons/120822


'''
문제 : 문자열 my_string이 매개변수로 주어집니다. 
      my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.
'''

def solution(my_string):
    answer = ''
    for i in my_string:
        answer = i + answer
    return answer
        