def solution(gems):
    gems_set = len(set(gems))  # {D, R, E, S}
    start, end = 0, 0
    check = {gems[0]: 1}
    answer = [0, 100001]
    # [0, len(gems)]하면 맨 밑에서 answer[1], answer[0] += 1씩 해주기 때문에 보석 쇼핑이 맨 마지막에서 끝나면 len(gems)=6이더라도 답이 [,7]로 나온다
    while start < len(gems)-1 and end < len(gems)-1:

        if len(check) < gems_set:
            end += 1
            if check.get(gems[end]) is None:  # 중복이 많아지면 n번 돌기때문에 효율성 꽝
                check[gems[end]] = 1
            else:
                check[gems[end]] += 1

        elif len(check) == gems_set:
            if answer[1] - answer[0] > end - start:
                answer[1] = end
                answer[0] = start
            if check[gems[start]] != 1:
                check[gems[start]] -= 1
                start += 1
            elif check[gems[start]] == 1:
                del check[gems[start]]
                start += 1

    answer[0] += 1
    answer[1] += 1

    return answer

gems=["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))