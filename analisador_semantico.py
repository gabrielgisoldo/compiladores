t_count = 1
def getTemp():
    """."""
    global t_count
    aux = t_count
    t_count += 1
    return str(aux)

def op_pri(op):
    """."""
    if op in ('*', '/'):
        return 2
    elif op in ('+', '-'):
        return 1
    else:
        return 0

class AnalisadorSemantico(object):
    """."""

    def __init__(self, expr, is_sub=False):
        """."""
        self.expr = expr
        self.operators = []
        self.numbers = []
        self.output = ''
        self.is_sub = is_sub

    def __repr__(self):
        """."""
        return str(vars(self))

    def add_num(self, num):
        """."""
        self.numbers.append(num)

    def add_op(self, op):
        """."""
        self.operators.append(op)

    def drop_num(self):
        """."""
        return self.numbers.pop()

    def drop_op(self):
        """."""
        return self.operators.pop()

    def eh_simbolo(self):
        """."""
        return self.expr.value() in ['+', '-', '*', '/']

    def gera_codigo(self):
        """."""
        a = self.drop_num()
        b = self.drop_num()
        o = self.drop_op()
        t = '#T%s' % getTemp()
        self.add_num(t)

        self.output += 'LDA %s\n' % b

        if o == '+':
            self.output += 'ADA %s\n' % a
        elif o == '-':
            self.output += 'SUB %s\n' % a
        elif o == '*':
            self.output += 'MUL %s\n' % a
        elif o == '/':
            self.output += 'DIV %s\n' % a
        else:
            raise Exception('Operador desconhecido')

        self.output += 'STA %s\n' % t

        if self.operators:
            self.gera_codigo()
        else:
            return

    def op_ok(self):
        """."""
        if not self.operators:
            return True
        elif op_pri(self.expr.value()) > op_pri(self.operators[-1]):
            return True
        else:
            return False

    def start(self):
        """."""
        return self.e0()

    def e0(self):
        """."""
        if self.expr.fim():
            self.gera_codigo()
            return
        elif self.expr.value() == '(':
            self.expr.up_index()
            sub = AnalisadorSemantico(self.expr, True)
            sub.start()
            self.output += sub.output
            self.add_num(sub.drop_num())
            self.e0()
        elif self.expr.value() == ')':
            self.expr.up_index()
            if self.is_sub:
                self.gera_codigo()
                return
        elif self.expr.value().isdigit():
            self.e1()
        elif self.eh_simbolo():
            self.e2()
        else:
            raise Exception(self.expr.value())

    def e1(self):
        """."""
        self.add_num(self.expr.value())
        self.expr.up_index()
        self.e0()

    def e2(self):
        """."""
        if self.op_ok():
            self.add_op(self.expr.value())
            self.expr.up_index()
        else:
            self.gera_codigo()

        self.e0()

class Expressao(object):
    """."""

    def __init__(self, expr):
        """."""
        self.expr = expr
        self.index = 0

    def up_index(self):
        self.index += 1

    def fim(self):
        """."""
        return self.index == len(self.expr)

    def value(self):
        """."""
        if not self.fim():
            return self.expr[self.index]
        else:
            return ''

    def __repr__(self):
        """."""
        return str(self)

    def __str__(self):
        """."""
        return str(vars(self))
