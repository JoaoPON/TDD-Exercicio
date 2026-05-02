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

def obter_sprite(corpo, dimensoes):
    # Diferença simples: atual - anterior
    dx = corpo[0][0] - corpo[1][0]
    dy = corpo[0][1] - corpo[1][1]
    
    if dx == 0 and dy == -1:
        return "head_up"
    return "body_horizontal"