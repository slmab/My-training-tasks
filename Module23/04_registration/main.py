# TODO здесь писать код

def check_errors(string):
    if len(string) != 3:
        raise IndexError
    elif not string[0].isalpha():
        raise NameError
    elif ('@' not in string[1]) or ('.' not in string[1]):
        raise SyntaxError
    elif not 10 < int(string[2]) < 99:
        raise ValueError
    else:
        return ' '.join(string)


with open('registrations.txt', 'r', encoding='utf-8') as registration_file:
    with open('registrations_good.log', 'w', encoding='utf-8') \
            as good_registration:
        with open('registrations_bad.log', 'w', encoding='utf-8') \
                as bad_registrations:
            for i_line in registration_file:
                try:
                    check_string = check_errors(i_line.rstrip().split())
                    good_registration.write(check_string + '\n')
                except IndexError:
                    bad_registrations.write(i_line.rstrip() +
                                            ' Errors: IndexError\n')
                except NameError:
                    bad_registrations.write(i_line.rstrip() +
                                            ' Errors: NameError\n')
                except SyntaxError:
                    bad_registrations.write(i_line.rstrip() +
                                            ' Errors: SyntaxError\n')
                except ValueError:
                    bad_registrations.write(i_line.rstrip() +
                                            ' Errors: ValueError\n')
