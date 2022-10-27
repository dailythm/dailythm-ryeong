# url : https://school.programmers.co.kr/learn/courses/30/lessons/120808


'''
문제 : 첫 번째 분수의 분자와 분모를 뜻하는 denum1, num1, 두 번째 분수의 분자와 분모를 뜻하는 denum2, num2가 매개변수로 주어집니다. 
      두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

'''

def solution(denum1, num1, denum2, num2):
    answer = [denum1*num2 + denum2*num1, num1*num2]
    for i in range(min(answer[0],answer[1]), 0, -1):
        if answer[0] % i == 0 and answer[1] % i == 0:
            answer = [answer[0] / i, answer[1] / i]
    return answer