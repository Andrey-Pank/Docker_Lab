import random
import math

## Проверка числа, является ли оно простым
def isPrime(num):
    if num < 2:
        return False
    cnt = 0
    for i in range(2, int(math.sqrt(num)+1)):
        if (0 == num % i):
            cnt += 1
    if cnt > 0:
        return False
    else:
        return True

##Генерация простого числа на заданном отрезке
def genRandomPrime(min, max):
    cachedPrimes = [i for i in range(min, max) if isPrime(i)]
    ##print(cachedPrimes)
    pr = random.choice(cachedPrimes)
    return pr

## Поиск взаимно простого числа
def PHI(num):
    totalsPrime = [i for i in range(1, num+1) if 1 == math.gcd(num, i)]
    ##print(totalsPrime)
    total = random.choice(totalsPrime)
    return total

## Генерация следующего числа в сверхвозрастающем массиве
def genNextNum(summa):
    if 0 == summa:
        out = random.randint(1, 27)
        return out
    start = int(summa)
    end = int(summa*1.68 + 2)
    cachedNums = [i for i in range(start + 1, end)]
    out = random.choice(cachedNums)
    return out

## Генерация сверх возрастающего секретного ключа
def genSecretKey(size):
    res = []
    elem = 0
    for i in range(0, size):
        sum = 0
        for j in range(0, len(res)):
            sum += int(res[j])
        elem = genNextNum(sum)
        res.append(elem)
    return res

## Создание открытого ключа на основе закрытого и двух простых чисел
def createOpenKey(secretkey, p, q):
    res = []
    for i in range(0, len(secretkey)):
        elem = int((secretkey[i] * q) % p)
        res.append(elem)
    return res

## Расширенный алготим Евклида
def gcdExtended(num1, num2):
    if 0 == num1:
        return (num2, 0, 1)
    else:
        div, x, y = gcdExtended(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)

def initPQR(min, max):
    res_p = genRandomPrime(min, max)
    res_q = PHI(res_p)
    gcdEArray = gcdExtended(res_q, res_p)
    res_r = gcdEArray[1]
    while (0 > res_r):
        res_q = PHI(res_p)
        gcdEArray = gcdExtended(res_q, res_p)
        res_r = gcdEArray[1]
    return res_p, res_q, res_r