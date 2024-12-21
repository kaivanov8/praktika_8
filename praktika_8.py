#новый
def calc(line):
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == '+':
        print(f'результат:{operand_1 + operand_2}')
    if operation == '-':
        print(f'результат:{operand_1 - operand_2}')
    if operation == '//':
        print(f'результат:{operand_1 // operand_2}')
    if operation == '/':
        print(f'результат:{operand_1 / operand_2}')
    if operation == '%':
        print(f'результат:{operand_1 % operand_2}')
    if operation == '*':
        print(f'результат:{operand_1 * operand_2}')

cnt = 0
with open('text_for_praktika_8.txt', 'r') as file:
    for line in file:
        cnt += 1
        try:
            calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'ошибка в строке - {cnt} (не хватаетданных для вычисления)')
            if 'invalid literal' in exc.args[0]:
                print(f'в втроке {cnt} неверный порядок данных')
             #   print(f'ошибка в строке {cnt}, возникло "{exc}" с параметрами {exc.args}')
