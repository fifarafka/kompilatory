from pythonds.basic.stack import Stack
import re


class Environment(object):
    def __init__(self, args):
        self.args = args
        self.path_pattern = re.compile("^(.)*\.py$")
        self.put_pattern = re.compile("^put ([0-9])+$")
        self.stack = Stack()

    def count(self):
        for arg in self.args:
            if (self.put_pattern.match(arg)):
                number = int(arg[4:])
                self.stack.push(number)

            elif (arg == 'add'):

                number_1 = self.stack.pop()
                number_2 = self.stack.pop()
                result = number_1 + number_2
                self.stack.push(result)

            elif (arg == 'sub'):

                number_1 = self.stack.pop()
                number_2 = self.stack.pop()
                result = number_2 - number_1
                self.stack.push(result)

            elif (arg == 'mul'):
                number_1 = self.stack.pop()
                number_2 = self.stack.pop()
                result = number_1 * number_2
                self.stack.push(result)

            elif (arg == 'div'):

                number_1 = self.stack.pop()
                number_2 = self.stack.pop()
                result = number_2 / number_1
                self.stack.push(result)

            elif (arg == 'end'):
                return self.stack.pop()

            elif (self.path_pattern.match(arg)):
                pass

            else:
                #jakies rzucanie wyjatkiem
                print 'I got some strange input here: %s' % arg