# TODO здесь писать код

def ceasar_code(some_string, shift):
    result = ''
    for letter in some_string:
        if (letter.isalpha()) and (letter.islower()):
            number = ord(letter) + shift % 26
            if number > 122:
                number -= 26
            result += chr(number)
        elif (letter.isalpha()) and (letter.isupper()):
            number = ord(letter) + shift % 26
            if number > 90:
                number -= 26
            result += chr(number)
        else:
            result += letter
    return result


task = open('text.txt', 'r')
new_code = ''
for index, line in enumerate(task, start=1):
    new_string = ceasar_code(line,  index)
    new_code += new_string

asnwer = open('text.txt', 'w')
asnwer.write(new_code)
asnwer.close()
