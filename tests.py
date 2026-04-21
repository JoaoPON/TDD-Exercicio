import snake_funcs

#Etapa 1 - Inicializar Jogo
def test_deve_inicializar_o_jogo_com_uma_cobra_e_uma_fruta():
    estado = snake_funcs.inicializar_jogo(largura=20, altura=10)

    assert "cobra" in estado
    assert estado["cobra"] == [(10,5),(9,5)]

    assert "frutas" in estado
    assert len(estado["frutas"]) == 1


#Etapa 2 - Mover Cobra
def test_mover_cobra():
    estado = snake_funcs.inicializar_jogo(20,10)

    estado["cobra"], estado["frutas"] = snake_funcs.mover_cobra(estado["cobra"], estado["frutas"], direcao="d")

    assert estado["cobra"][0] == (11,5)
    assert estado["cobra"][1] == (10,5)
    assert len(estado["cobra"]) == 2


#Etapa 3 - Comer Frutas e Crescer
def test_comer_para_poder_crescer():
    corpo = [(7,5), (6,5), (5,5)]
    frutas = [(8,5)]
    corpo, frutas = snake_funcs.mover_cobra(corpo, frutas, "d")
    assert len(corpo) == 4
    assert len(frutas) == 0

def test_nao_comer_para_nao_crescer():
    corpo = [(7,5), (6,5), (5,5)]
    frutas = [(1,1)]
    corpo, frutas = snake_funcs.mover_cobra(corpo, frutas, "d")
    assert len(corpo) == 3
    assert len(frutas) == 1

#Etapa 4 - Sistema de Colisão


#Etapa 5 - Atravessar Paredes


#Etapa 6 - Regras de Progressão


#Etapa 7 - Gerar Novas Frutas
