import random

def inicializar_jogo(largura, altura):
    meio_x = largura // 2
    meio_y = altura // 2
    return {
        "cobra": [(meio_x, meio_y),(meio_x-1,meio_y)],
        "frutas": [(meio_x + 3, meio_y)] # Fruta um pouco à frente
    }

def mover_cobra(corpo, frutas, direcao, dimensoes):
    largura, altura = dimensoes
    if direcao not in "wasd":
        return corpo, frutas
    x, y = corpo[0]
    if direcao == "d":
        nova_cabeca = (x+1,y)
        if nova_cabeca[0] > largura-1:
            nova_cabeca = (0,y)
    elif direcao == "w":
        nova_cabeca = (x,y-1)
        if nova_cabeca[1] < 0:
            nova_cabeca = (x,altura-1)
    elif direcao == "s":
        nova_cabeca = (x,y+1)
        if nova_cabeca[1] > altura-1:
            nova_cabeca = (x,0)
    elif direcao == "a":
        nova_cabeca = (x-1,y)
        if nova_cabeca[0] < 0:
            nova_cabeca = (largura-1,y)

    if nova_cabeca == corpo[1]:
        dx = x - corpo[1][0]
        dy = y - corpo[1][1]
        nova_cabeca = (x + dx, y + dy)

    if nova_cabeca in frutas:
        novo_corpo = [nova_cabeca] + corpo
        frutas.remove(nova_cabeca)
    else:
        novo_corpo = [nova_cabeca] + corpo[:-1]
    return novo_corpo, frutas

def gerar_frutas(dimensoes, corpo):
    largura, altura = dimensoes
    novas_frutas = []
    qta = 1
    if len(corpo) > 19:
        qta = 3
    elif len(corpo) > 9:
        qta = 2
    
    while len(novas_frutas) < qta:
        x = random.randint(0,largura-1)
        y = random.randint(0,altura-1)
        posicao = (x,y)

        if posicao not in corpo and posicao not in novas_frutas:
            novas_frutas.append(posicao)
    
    return novas_frutas

def colisao(corpo):
    return corpo[0] in corpo[1:]

def calcular_posicao(ponto_a, ponto_b, dimensoes):
    largura, altura = dimensoes
    dx = ponto_a[0] - ponto_b[0]
    dy = ponto_a[1] - ponto_b[1]

    if abs(dx) > largura / 2:
        dx = dx - largura if dx > 0 else dx + largura
    if abs(dy) > altura / 2:
        dy = dy - altura if dy > 0 else dy + altura
        
    return dx, dy

def obter_sprite(corpo, dimensoes, indice=0):
    atual = corpo[indice]
    
    if indice == 0 or indice == len(corpo) - 1:
        vizinho = corpo[1] if indice == 0 else corpo[indice - 1]
        prefixo = "head_" if indice == 0 else "tail_"
        
        delta = calcular_posicao(atual, vizinho, dimensoes)
        direcoes = {(0, -1): "up", (0, 1): "down", (-1, 0): "left", (1, 0): "right"}
        return prefixo + direcoes[delta]

    v_ant = calcular_posicao(corpo[indice - 1], atual, dimensoes)
    v_prox = calcular_posicao(corpo[indice + 1], atual, dimensoes)

    if v_ant[0] == v_prox[0]: return "body_vertical"
    if v_ant[1] == v_prox[1]: return "body_horizontal"

    mapeamento_curvas = {
        frozenset({(0, -1), (1, 0)}):  "body_topright",
        frozenset({(0, -1), (-1, 0)}): "body_topleft",
        frozenset({(0, 1), (1, 0)}):   "body_bottomright",
        frozenset({(0, 1), (-1, 0)}):  "body_bottomleft"
    }
    
    vizinhos = frozenset({v_ant, v_prox})
    return mapeamento_curvas[vizinhos]