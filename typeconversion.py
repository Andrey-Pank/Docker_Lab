## Перевод из тестового формата в числовой
def strToBits(text):
    res = str(''.join((format(ord(x), '08b') for x in text)))
    return res

## Разделение строки бит на блоки, заданной длины
def splitText(text, lenkey):
    res = []
    block = []
    for i in range(0, len(text)):
        if (lenkey != len(block)):
            block.append(int(text[i]))
        if (lenkey == len(block)):
            ##print(block)
            res.append(list(block))
            block.clear()
    return res

## Соединение блоков бит в строку
def concateText(blockText):
    row = len(blockText)
    res = ""
    for i in range(0, row):
        col = len(blockText[i])
        for j in range(0, col):
            res += str(blockText[i][j])
    return res

## Перевод из битов в символы
def bitsToStr(bitText):
    res = ""
    temp = ""
    for i in range(0, len(bitText)):
        if (8 != len(temp)):
            temp += bitText[i]
        if (8 == len(temp)):
            ##print(temp)
            res += chr(int(temp, 2))
            temp = ""
    return res
