# url : https://school.programmers.co.kr/learn/courses/30/lessons/120885


'''
문제 : 이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 
      두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

'''

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