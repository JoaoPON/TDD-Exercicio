import pygame
import snake_funcs

def rodar_jogo():
    dimensoes = (20, 10)
    tamanho_pixel = 40

    pygame.init()
    tela = pygame.display.set_mode((dimensoes[0]*tamanho_pixel, dimensoes[1]*tamanho_pixel))
    clock = pygame.time.Clock()

    sprites = {}
    nomes = [
        "head_up", "head_down", "head_left", "head_right",
        "tail_up", "tail_down", "tail_left", "tail_right",
        "body_horizontal", "body_vertical",
        "body_bottomleft", "body_bottomright", "body_topleft", "body_topright",
        "apple"
    ]
    for nome in nomes:
        sprites[nome] = pygame.image.load(f"Graphics/{nome}.png")

    estado_jogo = snake_funcs.inicializar_jogo(*dimensoes)
    direcao_atual = "d"

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit(); return
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w: direcao_atual = "w"
                if evento.key == pygame.K_s: direcao_atual = "s"
                if evento.key == pygame.K_a: direcao_atual = "a"
                if evento.key == pygame.K_d: direcao_atual = "d"

        estado_jogo["cobra"], estado_jogo["frutas"] = snake_funcs.mover_cobra(
            estado_jogo["cobra"], estado_jogo["frutas"], direcao_atual, dimensoes
        )
        
        if snake_funcs.colisao(estado_jogo["cobra"]):
            print(f"Game Over! Pontuação: {len(estado_jogo['cobra'])-2}")
            pygame.quit(); return

        if len(estado_jogo["frutas"]) == 0:
            estado_jogo["frutas"] = snake_funcs.gerar_frutas(dimensoes, estado_jogo["cobra"])

        tela.fill((50, 50, 50))

        for fx, fy in estado_jogo["frutas"]:
            tela.blit(sprites["apple"], (fx * tamanho_pixel, fy * tamanho_pixel))

        for i in range(len(estado_jogo["cobra"])):
            x, y = estado_jogo["cobra"][i]

            nome_sprite = snake_funcs.obter_sprite(estado_jogo["cobra"], dimensoes, i)
            tela.blit(sprites[nome_sprite], (x * tamanho_pixel, y * tamanho_pixel))

        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    rodar_jogo()