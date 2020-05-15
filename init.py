# Gabriel Diniz Gisoldo RA: 22214007-1
# import analisador_v2 as analisador_mod
import analisador_semantico

# Pega o input
tape = input("Digite a palavra: ")
# tape += ' '
tape = tape.replace(' ', '')

# Instancia a expressao
expr = analisador_semantico.Expressao(expr=tape)
maq = analisador_semantico.AnalisadorSemantico(expr)
maq.start()

# print(maq.output)
print(maq.output)

# Executa o nalisador lexico
# analisador = analisador_semantico.AnalisadorSemantico(expr)

# Espera um input do usuario para encerrar o programa
input('')
