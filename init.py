# Gabriel Diniz Gisoldo RA: 22214007-1
# import analisador_v2 as analisador_mod
import analisador_sintatico

# Pega o input
tape = input("Digite a palavra: ")
# tape += ' '
tape = tape.replace(' ', '')

# Instancia o analisador lexico
analisador = analisador_sintatico.AnalisadorSintatico(tape)
# Executa o nalisador lexico
analisador.start()

# Espera um input do usuario para encerrar o programa
input('')
