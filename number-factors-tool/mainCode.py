print("welcome to prime numbers explorer")
inputStr = input("num:").strip()


def checkIfInput(string):
    try:
        num = int(string)
        print("Working:")
        return num
    except ValueError:
        print("ERROR: Please enter a valid number")
        global inputStr
        inputStr = new_input = input("num:").strip()
        # Return the result of the recursive call
        return checkIfInput(new_input)


def checkIfNum(num):
    if num > 1000000:
        return False
    return True


def getPrimeFactors(inputStr):
    result = []
    inputStr = int(inputStr)
    i = 2

    while i*i <= inputStr:
        if inputStr % i == 0:

            inputStr //= i
            result.append(i)
        else:
            i += 1
    if inputStr > 1:
        result.append(inputStr)
    return result


def getAllFactors(n):
    n = int(n)
    result = []
    if not checkIfNum(n):
        print("sorry but this number is very big our maxiumum is 1 million")
    return [i for i in range(1, n + 1) if n % i == 0]
    # for num in range(1, inputStr):
    #     if inputStr % num == 0:
    #         result.append(num)
    # result.append(inputStr)

    # return result


if checkIfInput(inputStr):
    all_factors = getAllFactors(inputStr)
    prime_factors = getPrimeFactors(inputStr)
    print("All factors:", all_factors)
    print("Prime factors:", prime_factors)
