# url : https://school.programmers.co.kr/learn/courses/30/lessons/120863


'''
문제 : 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 
      덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 
      같은 식이라면 가장 짧은 수식을 return 합니다.

'''

def solution(polynomial):
    answer = []
    linear, const = 0, 0
    
    for i in polynomial.split(' + '):
        if i.isdigit() : const += int(i)
        elif i == 'x' : linear += 1 
        else : linear += int(i[:-1])
            
    if linear == 1 : answer.append('x')
    elif linear > 1 : answer.append(str(linear) + 'x')
    if const > 0 : answer.append(str(const))
    
    return ' + '.join(answer)