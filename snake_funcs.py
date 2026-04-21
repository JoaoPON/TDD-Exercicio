def inicializar_jogo(largura, altura):
    meio_x = largura // 2
    meio_y = altura // 2
    return {
        "cobra": [(meio_x, meio_y),(meio_x-1,meio_y)],
        "frutas": [(meio_x + 3, meio_y)] # Fruta um pouco à frente
    }

def mover_cobra(corpo, direcao):
    if direcao == "d":
        corpo_novo = [(11,5),(10,5)]
        return corpo_novo
    return corpo