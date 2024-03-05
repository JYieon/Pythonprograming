def solution(shirt_size):
    
    XS = 0
    S = 0
    M = 0
    L = 0
    XL = 0
    XXL = 0

    for i in shirt_size:
        if i == "XS":
            XS += 1
        elif i == "S":
            S += 1
        elif i == "M":
            M += 1
        elif i == "L":
            L += 1
        elif i == "XL":
            XL += 1
        elif i == "XXL":
            XXL += 1
    answer = [XS, S, M, L, XL, XXL]
    return answer

#The following is code to output testcase.
shirt_size = ["XS", "S", "M", "L", "XL", "XXL"]
ret = solution(shirt_size);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")