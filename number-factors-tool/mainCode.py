print("welcome to prime numbers explorer")
inputNum = input("num:")


def checkIf(num):
    if num > 1000000:
        return False
    return True


def getNumberFactores(inputNum):
    inputNum = int(inputNum.strip())
    result = []
    if checkIf(inputNum):
        for num in range(1, inputNum):
            if inputNum % num == 0:
                result.append(num)
        result.append(inputNum)
        return result
    print("sorry but this number is very big our maxiumum is 1 million")


def getPrimeFactores(inputNum):
    result = []
    inputNum = int(inputNum.strip())
    i = 2

    while i*i <= inputNum:
        if inputNum % i == 0:

            inputNum //= i
            result.append(i)
        else:
            i += 1
    if inputNum > 1:
        result.append(inputNum)
    return result


print(getNumberFactores(inputNum))
print(getPrimeFactores(inputNum))