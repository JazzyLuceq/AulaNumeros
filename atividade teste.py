import random as rd

def jogo_adivinhacao():
    numero_secreto = rd.randint(1, 100)
    tentativas = 0
    
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")
    
    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1
            
            if palpite < 1 or palpite > 100:
                print("Por favor, digite um número entre 1 e 100.")
            elif palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")

if __name__ == "__main__":
    jogo_adivinhacao()
