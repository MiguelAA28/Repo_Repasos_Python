# RETO PYTHON

i = 1

while i <= 250:
    print(i)
    i = i + 1

with open('result.txt', 'w') as fOut:
    line1 = 'i = 1\n'
    fOut.write(line1)

    line2 = 'While i <= 1250:\n'
    fOut.write(line2)

    line3 = 'print(i)\n'
    fOut.write(line3)

    line4 = 'i = i + 1\n'
    fOut.write(line4)

    fOut.close()