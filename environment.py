from pythonds.basic.stack import Stack
import sys
import re

path_pattern = re.compile("^(.)*\.py$")
put_pattern = re.compile("^put ([0-9])+$")

s = Stack()

for arg in sys.argv:
    if(put_pattern.match(arg)):
        number = int(arg[4:])
        print 'I got a put command here with number: %d' % number

        s.push(number)

    elif(arg == 'add'):
        print 'I got an add command here'

        number_1 = s.pop()
        number_2 = s.pop()

        result = number_1 + number_2

        s.push(result)

    elif(arg == 'mul'):
        print 'I got a multiply command here'

        number_1 = s.pop()
        number_2 = s.pop()

        result = number_1 * number_2

        s.push(result)

    elif( arg == 'end'):
        print 'I got an end command here and the result is: %d' % s.pop()

    # pierwszy argument to zawsze sciezka do skryptu - pomijamy
    elif( path_pattern.match(arg) ):
        pass

    else:
        print 'I got some unknown shit here: %s' % arg