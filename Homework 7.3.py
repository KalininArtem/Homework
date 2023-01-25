with open('data_homework7.3/txt1.txt', 'r', encoding='utf-8') as file1:
    num1 = file1.read()
with open('data_homework7.3/txt1.txt', 'r', encoding='utf-8') as file1:
    count1 = 0
    for i in file1:
        count1 += 1

with open('data_homework7.3/txt2.txt', 'r', encoding='utf-8') as file2:
    num2 = file2.read()
with open('data_homework7.3/txt2.txt', 'r', encoding='utf-8') as file2:
    count2 = 0
    for i in file2:
        count2 += 1

with open('data_homework7.3/txt3.txt', 'r', encoding='utf-8') as file3:
    num3 = file3.read()
with open('data_homework7.3/txt3.txt', 'r', encoding='utf-8') as file3:
    count3 = 0
    for i in file3:
        count3 += 1

with open('data_homework7.3/result.txt', 'wt', encoding='utf-8') as result:
    if count1 > count2 > count3:
        result.write('txt3\n')
        result.write(f'{count3}\n')
        result.write(f'{num3}\n')
        result.write('txt2\n')
        result.write(f'{count2}\n')
        result.write(f'{num2}\n')
        result.write(f'txt1\n')
        result.write(f'{count1}\n')
        result.write(f'{num1}\n')
        result.write('\n')
    elif count1 > count3 > count2:
        result.write('txt2\n')
        result.write(f'{count2}\n')
        result.write(f'{num2}\n')
        result.write('txt3\n')
        result.write(f'{count3}\n')
        result.write(f'{num3}\n')
        result.write(f'txt1]\n')
        result.write(f'{count1}\n')
        result.write(f'{num1}\n')
        result.write('\n')
    elif count2 > count1 > count3:
        result.write('txt3\n')
        result.write(f'{count3}\n')
        result.write(f'{num3}\n')
        result.write('txt1\n')
        result.write(f'{count1}\n')
        result.write(f'{num1}\n')
        result.write('txt2\n')
        result.write(f'{count2}\n')
        result.write(f'{num2}\n')
        result.write('\n')
    elif count2 > count3 > count1:
        result.write('txt1\n')
        result.write(f'{count1}\n')
        result.write(f'{num1}\n')
        result.write('txt3\n')
        result.write(f'{count3}\n')
        result.write(f'{num3}\n')
        result.write('txt2\n')
        result.write(f'{count2}\n')
        result.write(f'{num2}\n')
        result.write('\n')
    elif count3 > count1 > count2:
        result.write('txt2\n')
        result.write(f'{count2}\n')
        result.write(f'{num2}\n')
        result.write('txt1\n')
        result.write(f'{count1}\n')
        result.write(f'{num1}\n')
        result.write('txt3\n')
        result.write(f'{count3}\n')
        result.write(f'{num3}\n')
    elif count3 > count2 > count1:
        result.write('txt1\n')
        result.write(f'{count1}\n')
        result.write(f'{num1}\n')
        result.write('txt2\n')
        result.write(f'{count2}\n')
        result.write(f'{num2}\n')
        result.write('txt3\n')
        result.write(f'{count3}\n')
        result.write(f'{num3}\n')
        result.write('\n')
