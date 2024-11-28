def calcular_velocidade_media():
    distancia = float(input("Digite a distância percorrida (em km): "))
    tempo = float(input("Digite o tempo gasto (em horas): "))
    
    velocidade_media = distancia / tempo
    print(f"A velocidade média é {velocidade_media} km/h")

calcular_velocidade_media()