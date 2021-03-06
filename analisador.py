class Analisador(object):
    """Analisador lexico."""

    def __init__(self):
        self.tape = ''
        self.index = 0
        self.tempS = ''
        self.tabVar = []
        self.output = ''

    def isBlank(self):
        """."""
        return self.tape[self.index] == ' '

    def contain(self):
        """."""
        for index, value in enumerate(self.tabVar):
            if value == self.tempS:
                return index
        return -1

    def up_index(self):
        """."""
        self.index += 1

    def tabela(self):
        """."""
        for index, value in enumerate(self.tabVar):
            print('%s ... %s' % (index, value))

    def sigma1(self):
        """."""
        self.tempS = self.tape[self.index]

    def sigma2(self):
        """."""
        self.tempS = self.tempS + self.tape[self.index]

    def sigma3(self):
        """."""
        if len(self.tabVar) == 0:
            self.tabVar.append(self.tempS)
            self.output += 'V(%s)' % (len(self.tabVar) - 1)
        else:
            tmp = self.contain()
            if tmp >= 0:
                self.output += 'V(%s)' % (tmp)
            else:
                self.tabVar.append(self.tempS)
                self.output += 'V(%s)' % (len(self.tabVar) - 1)

    def sigma4(self):
        """."""
        self.tempN = int(self.tape[self.index])

    def sigma5(self):
        """."""
        self.tempN = (self.tempN * 10) + int(self.tape[self.index])

    def sigma6(self):
        """."""
        self.output += 'N(%s)' % (self.tempN)

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
        else:
            raise Exception("REJEITADO")

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

    def main(self):
        """."""
        self.tape = input("Digite a palavra: ")
        self.tape += ' '
        self.e0()
        input('')
        return

analisador = Analisador()
analisador.main()
