import software as sw
import typeconversion as tc

def encrypt(text, key):
    row = len(text)
    col = len(key)
    res = []
    for i in range(0, row):
        c = 0
        for j in range(0, col):
            c += key[j] * int(text[i][j])
        res.append(c)
    return res

def decrypt(cypher, key, r, p):
    res = []
    for i in range(0, len(cypher)):
        blokcs = []
        temp = (cypher[i] * r) % p
        for j in range(len(key)-1, -1, -1):
            ##print(key[j], temp)
            if (0 == temp) or (temp < key[j]):
                blokcs = [int(0)] + blokcs
            elif (temp >= key[j]):
                temp -= key[j]
                blokcs = [int(1)] + blokcs
        res.append(list(blokcs))
    return res

def start(text):
    bitText = tc.strToBits(text)
    ##print(bitText)
    spBitText = tc.splitText(bitText, 4)
    ##print(spBitText)
    sKey = list(sw.genSecretKey(4))
    print("Закрытый ключ: ", sKey)
    sumSKey = sum(sKey)
    ##print("Сумма элементов ключа:", sumSKey)
    resInit = sw.initPQR(sumSKey, 1000)
    p = resInit[0]
    print("Простое число:", p)
    q = resInit[1]
    print("Взаимнопростое число:", q)
    r = resInit[2]
    print("Мультипликативное обратное:", r)
    oKey = sw.createOpenKey(sKey, p, q)
    print("Открытый ключ: ", oKey)
    cText = encrypt(spBitText, oKey)
    print("Зашифрованное сообщение:", cText)
    origText = decrypt(cText, sKey, r, p)
    ##print("Расшифрованный текст:", origText)
    origText = tc.concateText(origText)
    ##print("Расшифрованный текст:", origText)
    origText = tc.bitsToStr(origText)
    print("Расшифрованный текст:", origText)