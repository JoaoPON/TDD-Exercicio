def inicializar_jogo(largura, altura):
    meio_x = largura // 2
    meio_y = altura // 2
    return {
        "cobra": [(meio_x, meio_y),(meio_x-1,meio_y)],
        "frutas": [(meio_x + 3, meio_y)] # Fruta um pouco à frente
    }