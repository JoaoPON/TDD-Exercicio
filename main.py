import time
from snake_screen import io_handler

def rodar_jogo():
    # 1. Configurações iniciais
    dimensoes = (20, 10)
    velocidade = 0.2
    
    interface = io_handler(dimensoes, velocidade)
    #estado_jogo = inicializar_jogo(dimensoes) # Retorna um dict com cobra, frutas, etc.
    
    interface.record_inputs() # Começa a ouvir o teclado

    while True:
        # 2. Captura a direção do teclado (input do prof)
        direcao = interface.last_input
        if direcao == 'end':
            break

        # 6. Exibe o resultado
        interface.display()
        
        # 7. Pausa para o próximo frame
        time.sleep(interface.game_speed)

if __name__ == "__main__":
    rodar_jogo()