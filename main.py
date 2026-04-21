import time, snake_funcs
from snake_screen import io_handler

def rodar_jogo():
    # 1. Configurações iniciais
    dimensoes = (20, 10)
    velocidade = 0.2
    
    interface = io_handler(dimensoes, velocidade)

    estado_jogo = snake_funcs.inicializar_jogo(dimensoes)
    
    interface.record_inputs() # Começa a ouvir o teclado

    while True:
        # 2. Captura a direção do teclado
        direcao = interface.last_input
        if direcao == 'end':
            break
        
        # Pinta a cobra na matriz usando os dados do 'estado_jogo'
        for x, y in estado_jogo["cobra"]:
            interface.matrix[y][x] = 2 # 2 é cabeça
            
        for x, y in estado_jogo["frutas"]:
            interface.matrix[y][x] = 3 # 3 é fruta

        # 3. Exibe o resultado
        interface.display()
        
        # 4. Pausa para o próximo frame
        time.sleep(interface.game_speed)

if __name__ == "__main__":
    rodar_jogo()