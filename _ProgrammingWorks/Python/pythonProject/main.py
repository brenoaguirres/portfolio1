# importa a biblioteca VPython
from vpython import *
scene = canvas(title='main', width=1300, height=700, background=color.gray(0.7))
# define as constantes físicas
altura_inicial = -10  # de -99 a 99
velocidade_inicial = vector(0.0, 0.0, 0.0)  # m/s
aceleracao_gravidade = 9.81
intervalo_tempo = 0.2  # s
massa_especifica_fluido = 2
massa_objeto = 1.8


# define o objeto como uma esfera
objeto = sphere(pos=vector(0, 0, 0), radius=7)
objeto.velocity = velocidade_inicial
objeto.pos.y = altura_inicial
objeto.velocity = objeto.velocity

# define o recipiente como como uma caixa
recipiente = box(pos=vector(0, 0, 0), size=vector(50, 200, 50), color=color.blue, opacity=0.2)
superficie = recipiente.size.y/2
fundo = -(recipiente.size.y/2)

# fórmula da força de empuxo:
y_empuxo = ((massa_especifica_fluido / massa_objeto) - 1) * aceleracao_gravidade
aceleracao_empuxo = vector(0.0, y_empuxo, 0.0)  # m/s^2

# parâmetros para calcular aceleração quando o objeto alcançar a superfície
h = superficie - (objeto.pos.y - objeto.radius)
incremento = 0.01
y_aceleracao_superficie = (((massa_especifica_fluido / massa_objeto) * log(h / (h + incremento)))-1) * aceleracao_gravidade
aceleracao_superficie = vector(0.0, y_aceleracao_superficie, 0.0)

# define o intervalo de tempo para a animação
rate(10)

# simula a queda livre do objeto
while (objeto.pos.y < (superficie)) and (objeto.pos.y > fundo + objeto.radius):  # estabelece uma condição de posição do objeto
     # atualiza a posição do objeto
    objeto.pos += objeto.velocity * intervalo_tempo + aceleracao_empuxo * (intervalo_tempo ** 2)
    # atualiza a velocidade do objeto
    objeto.velocity += aceleracao_empuxo * intervalo_tempo
    # aguarda um intervalo de tempo para animar o movimento
    rate(50)

    while (objeto.pos.y) > (superficie - objeto.radius):

        # atualiza a posição do objeto
        objeto.pos += objeto.velocity * intervalo_tempo + aceleracao_superficie * (intervalo_tempo ** 2)
        # atualiza a velocidade do objeto
        objeto.velocity += aceleracao_superficie * intervalo_tempo
        # aguarda um intervalo de tempo para animar o movimento
        rate(50)
