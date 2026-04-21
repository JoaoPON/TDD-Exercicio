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

    estado["cobra"] = snake_funcs.mover_cobra(estado["cobra"], direcao="d")

    assert estado["cobra"][0] == (11,5)
    assert estado["cobra"][1] == (10,5)
    assert len(estado["cobra"]) == 2
