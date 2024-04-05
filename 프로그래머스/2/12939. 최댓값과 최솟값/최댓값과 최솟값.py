def solution(s):
    data = [int(num) for num in s.split(' ')]
    answer = str(min(data))+' '+str(max(data))
    return answer