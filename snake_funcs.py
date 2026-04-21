def inicializar_jogo(largura, altura):
    meio_x = largura // 2
    meio_y = altura // 2
    return {
        "cobra": [(meio_x, meio_y),(meio_x-1,meio_y)],
        "frutas": [(meio_x + 3, meio_y)] # Fruta um pouco à frente
    }

def mover_cobra(corpo, frutas, direcao):
    if direcao not in "wasd":
        return corpo, frutas
    x, y = corpo[0]
    if direcao == "d":
        nova_cabeca = (x+1,y)
    elif direcao == "w":
        nova_cabeca = (x,y-1)
    elif direcao == "s":
        nova_cabeca = (x,y+1)
    elif direcao == "a":
        nova_cabeca = (x-1,y)
    if nova_cabeca in frutas:
        novo_corpo = [nova_cabeca] + corpo
        frutas.remove(nova_cabeca)
    else:
        novo_corpo = [nova_cabeca] + corpo[:-1]
    return novo_corpo, frutas