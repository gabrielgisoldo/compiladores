class Analisador(object):
    """docstring for Analisador."""

    def __init__(self):
        self.tape = ''
        self.index = 0
        self.tempS = ''
        self.tempC = ''
        self.tab = []
        self.tabP = ['IF', 'THEN', 'ELSE', 'GOTO', 'LET', 'END', 'PRINT',
                     'READ', 'OF']
        self.output = ''

    def isBlank(self):
        """."""
        return self.tape[self.index] == ' '

    def contain(self, res=0):
        """."""
        if not res:
            for index, value in enumerate(self.tab):
                if value == self.tempS:
                    return index
        else:
            for index, value in enumerate(self.tabP):
                if value == self.tempS:
                    return index
        return -1

    def up_index(self):
        """."""
        self.index += 1

    def tabela(self):
        """."""
        for index, value in enumerate(self.tab):
            print('%s ... %s' % (index, value))

    def sigma1(self):
        """."""
        self.tempS = self.tape[self.index]

    def sigma2(self):
        """."""
        self.tempS = self.tempS + self.tape[self.index]

    def sigma3(self):
        """."""
        tmp = self.contain(res=1)
        if tmp >= 0:
            self.output += 'P(%s)' % tmp
        else:
            if len(self.tab) == 0:
                self.tab.append(self.tempS)
                self.output += 'V(%s)' % (len(self.tab) - 1)
            else:
                tmp = self.contain()
                if tmp >= 0:
                    self.output += 'V(%s)' % (tmp)
                else:
                    self.tab.append(self.tempS)
                    self.output += 'V(%s)' % (len(self.tab) - 1)

    def sigma4(self):
        """."""
        self.tempN = int(self.tape[self.index])

    def sigma5(self):
        """."""
        self.tempN = (self.tempN * 10) + int(self.tape[self.index])

    def sigma6(self):
        """."""
        self.output += 'N(%s)' % (self.tempN)

    def sigma7(self):
        """."""
        self.output += ':'

    def sigma8(self):
        """."""
        self.output += ':='

    def sigma9(self):
        """."""
        self.tempC = self.tape[self.index]

    def sigma10(self):
        """."""
        self.output += self.tempC

    def e0(self):
        """."""
        if self.index == len(self.tape):
            print(self.output)
            self.tabela()
        elif(self.isBlank()):
            self.up_index()
            self.e0()
        elif self.tape[self.index].isdigit():
            self.sigma4()
            self.up_index()
            self.e2()
        elif self.tape[self.index].isalpha():
            self.sigma1()
            self.up_index()
            self.e1()
        elif self.tape[self.index] == ':':
            self.up_index()
            self.e3()
        elif self.tape[self.index] == '%':
            self.up_index()
            self.e6()
        else:
            self.e5()

    def e1(self):
        """."""
        if self.tape[self.index].isdigit() or self.tape[self.index].isalpha():
            self.sigma2()
            self.up_index()
            self.e1()
        else:
            self.sigma3()
            self.e0()

    def e2(self):
        """."""
        if self.tape[self.index].isdigit():
            self.sigma5()
            self.up_index()
            self.e2()
        else:
            self.sigma6()
            self.e0()

    def e3(self):
        """."""
        if self.tape[self.index] == '=':
            self.up_index()
            self.e4()
        else:
            self.sigma7()
            self.e0()

    def e4(self):
        """."""
        self.sigma8()
        self.e0()

    def e5(self):
        """."""
        self.sigma9()
        self.up_index()
        self.sigma10()
        self.e0()

    def e6(self):
        """."""
        if self.index == len(self.tape):
            self.e0()
        else:
            self.up_index()
            self.e6()

    def main(self):
        """."""
        self.tape = input("Digite a palavra: ")
        self.tape += ' '
        self.e0()
        input('')
        return

analisador = Analisador()
analisador.main()
