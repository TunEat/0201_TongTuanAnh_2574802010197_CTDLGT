T = [73, 74, 75, 71, 69, 72, 76, 73]

def dailyTemperature(T):
    stack = []
    answer = [0] * len(T)

    for i in range(len(T)):
        while stack and T[i] > T[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    return answer

print(dailyTemperature(T))