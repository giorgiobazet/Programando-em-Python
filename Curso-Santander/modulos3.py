import modulos_operacoes
import modulos_utilidades

resultado = modulos_operacoes.soma(10, 5)
modulos_utilidades.imprimir_mensagem(f"A soma é: {resultado}")

nome = modulos_utilidades.obter_usuario()
modulos_utilidades.imprimir_mensagem(f"Olá, {nome}!")
