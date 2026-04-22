import time, snake_funcs
from snake_screen import io_handler

def rodar_jogo():
    # 1. Configurações iniciais
    dimensoes = (20, 10)
    velocidade = 0.2
    
    interface = io_handler(dimensoes, velocidade)

    estado_jogo = snake_funcs.inicializar_jogo(*dimensoes)
    
    interface.record_inputs() # Começa a ouvir o teclado

    while True:
        direcao = interface.last_input
        interface.display()
        print("mova com WASD, saia com esc. Ultimo botão:", end=' ')
        
        ###adicione seu código para lidar com o jogo aqui
        
        #Movimento o corpo da cobra
        estado_jogo["cobra"], estado_jogo["frutas"] = snake_funcs.mover_cobra(estado_jogo["cobra"], estado_jogo["frutas"],interface.last_input, dimensoes)
        if snake_funcs.colisao(estado_jogo["cobra"]):
            exit()
        if len(estado_jogo["frutas"]) == 0:
            estado_jogo["frutas"] = snake_funcs.gerar_frutas(dimensoes, estado_jogo["cobra"])
        #Limpa a matrix para o próximo frame
        interface.matrix = [[0 for _ in range(dimensoes[0])] for _ in range(dimensoes[1])]

        #Todas as posições são corpo
        for x, y in estado_jogo["cobra"]:
            interface.matrix[y][x] = 1 # 1 é corpo

        #primeira posição é a cabeça
        cabeca_x, cabeca_y = estado_jogo["cobra"][0]
        interface.matrix[cabeca_y][cabeca_x] = 2 # 2 é cabeça

        for x, y in estado_jogo["frutas"]:
            interface.matrix[y][x] = 3 # 3 é fruta


        print(direcao)
        print(f"Pontuação {len(estado_jogo["cobra"])-2}")
        if(direcao == 'end'):
            exit()
        time.sleep(velocidade)

if __name__ == "__main__":
    rodar_jogo()