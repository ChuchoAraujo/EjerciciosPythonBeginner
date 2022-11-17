# Your code here!!
def sing():
    letra = ''
    for i in range(11):
        if i == 4:
            letra += 'whisper words of wisdom, '
        elif i == 10:
            letra += 'there will be an answer, let it be'
        else:
            letra += 'let it be, '
    return letra

print(sing())

