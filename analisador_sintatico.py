# Gabriel Diniz Gisoldo RA: 22214007-1
class AnalisadorSintatico(object):
    """Analisador sintatico."""

    def __init__(self, string, idx=0):
        self.string = string
        self.idx = idx
        self.pilha = 0

    def print_log(self):
        """."""
        print(vars(self))

    def up_index(self):
        """."""
        self.idx += 1

    def eh_simbolo(self):
        """."""
        return self.string[self.idx] in ['+', '-', '*', '/', '=']

    def fim_string(self):
        """."""
        return self.idx == len(self.string)

    def rejeita(self):
        """."""
        raise Exception('REJEITA')

    def start(self):
        """."""
        self.e0()

    def e0(self):
        """."""
        # self.print_log()
        if self.fim_string():
            self.rejeita()
        elif self.string[self.idx] == 'N':
            self.up_index()
            self.e1()
        elif self.string[self.idx] == 'I':
            self.up_index()
            self.e1()
        elif self.string[self.idx] == '(':
            self.up_index()
            self.e2()
        else:
            self.rejeita()

    def e1(self):
        """."""
        # self.print_log()
        if self.pilha == 0:
            if self.fim_string():
                print("ACEITO")
            elif self.eh_simbolo():
                self.up_index()
                self.e0()
            else:
                self.rejeita()
        else:
            if self.fim_string():
                self.rejeita()
            elif self.eh_simbolo():
                self.up_index()
                self.e0()
            elif self.string[self.idx] == ')':
                return
            else:
                self.rejeita()

    def e2(self):
        """."""
        # self.print_log()
        if self.fim_string():
            self.rejeita()
        else:
            self.pilha += 1
            self.e0()
            self.pilha -= 1
            self.e3()

    def e3(self):
        """."""
        if self.fim_string():
            self.rejeita()
        elif self.string[self.idx] == ')':
            self.up_index()
            self.e1()
        else:
            self.rejeita()
