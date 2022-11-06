# url : https://school.programmers.co.kr/learn/courses/30/lessons/120895


'''
문제 : 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, 
      my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.

'''

def solution(txt, num1, num2):
    if num1 > num2 : big, small = num1, num2
    else : big, small = num2, num1
    return txt[:small] + txt[big] + txt[small+1:big] + txt[small] + txt[big+1:]