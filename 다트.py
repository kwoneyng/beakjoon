def solution(dartResult):
    dartResult = list(dartResult)
    n = len(dartResult)
    s = 0
    calc = []
    while n > s:
        num = ''
        bonus = ''
        option = ''
        while not dartResult[s].isalpha():
            num += dartResult[s]
            s += 1
        bonus = dartResult[s]
        s += 1
        if n > s:
            if dartResult[s].isdigit():
                pass
            else:
                option = dartResult[s]
                s += 1
        num = int(num) 
        if bonus == 'S':
            pass
        elif bonus == 'D':
            num = num**2
        else:
            num = num**3
        if option == '*':
            if calc:
                calc[-1] *= 2
                num *= 2
            else:
                num *= 2
        elif option == '#':
            num *= -1
        calc.append(num)
        
    return sum(calc)

dartResult = '1S2D*3T'
print(solution(dartResult))