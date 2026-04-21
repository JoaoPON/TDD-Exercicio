import time
from snake_screen import io_handler

def rodar_jogo():
    # 1. Configurações iniciais
    dimensoes = (20, 10)
    velocidade = 0.2
    
    interface = io_handler(dimensoes, velocidade)
    
    interface.record_inputs() # Começa a ouvir o teclado

    while True:
        # 2. Captura a direção do teclado
        direcao = interface.last_input
        if direcao == 'end':
            break

        # 3. Exibe o resultado
        interface.display()
        
        # 4. Pausa para o próximo frame
        time.sleep(interface.game_speed)

if __name__ == "__main__":
    rodar_jogo()