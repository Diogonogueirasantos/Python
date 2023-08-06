def conversordetempo(x):
    minutos = 0.060
    convert = x * minutos
    print(f'O seu tempo de {x} minutos convertidos para segundos é {convert:.3f} segundos')



conversordetempo(60)


def medidordedistancia(y):
    milha = 1.61
    distancia_percorrida = y * milha
    print(f'A distancia percorrida foi {distancia_percorrida:.2f}')


medidordedistancia(10)



def passomedio():
    x = 16.10 / (3.600 + 0.42) 
    print(f'O velocidade media percorrido foi {x:.2f}')


passomedio()





