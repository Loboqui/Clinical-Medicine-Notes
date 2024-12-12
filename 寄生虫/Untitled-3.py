steps = [99999] * 50000005
num1 = [0] * 50000005
num2 = [0] * 50000005

steps[0] = 0
steps[2] = 0
steps[4] = 0
steps[8] = 0
steps[24] = 0

hierarchy = [[2, 4, 8, 24]]

for step in range(1, 10):
    print(f'Now numbers within {step} steps:')
    hierarchy.append([])
    if steps[114514] < 99998:
        print(f'Done! 114514 within{steps[114514]} steps!')
        break
    for i in range(0, round(step / 2 + 0.1)):
        j = step - i - 1
        print(f'    calc {i}steps, {j}steps to {step}steps:')
        for numA in hierarchy[i]:
            for numB in hierarchy[j]:
                if numA > numB:
                    a, b = numA, numB
                else:
                    a, b = numB, numA

                if step < steps[a + b]:
                    steps[a + b] = step
                    num1[a + b] = a
                    num2[a + b] = b
                    hierarchy[step].append(a + b)
                if step < steps[a - b]:
                    steps[a - b] = step
                    num1[a - b] = a
                    num2[a - b] = b
                    hierarchy[step].append(a - b)
                if a*b < 50000004 and step < steps[a*b]: # 这里剪枝可能数学证明上有问题
                    steps[a*b] = step
                    num1[a*b] = a
                    num2[a*b] = b
                    hierarchy[step].append(a*b)
                if a%b == 0 and step < steps[round(a/b)]:
                    steps[round(a/b)] = step
                    num1[round(a/b)] = a
                    num2[round(a/b)] = b
                    hierarchy[step].append(round(a/b))