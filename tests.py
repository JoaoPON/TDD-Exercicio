from snake_funcs import inicializar_jogo

#Etapa 1
def test_deve_inicializar_o_jogo_com_uma_cobra_e_uma_fruta():
    estado = inicializar_jogo(largura=20, altura=10)

    assert "cobra" in estado
    assert estado["cobra"] == [(10,5)]

    assert "frutas" in estado
    assert len(estado["frutas"]) == 1