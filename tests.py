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

#Etapa 4 - Gerar Novas Frutas
def test_gerar_frutas_deve_retornar_quantidade_correta():
    dimensoes = (20, 10)
    
    corpo_pequeno = [(0,0)]
    frutas_1 = snake_funcs.gerar_frutas(dimensoes, corpo_pequeno)
    assert len(frutas_1) == 1

    corpo_medio = [(i, 0) for i in range(10)] 
    frutas_2 = snake_funcs.gerar_frutas(dimensoes, corpo_medio)
    assert len(frutas_2) == 2

    corpo_grande = [(i, 0) for i in range(20)]
    frutas_3 = snake_funcs.gerar_frutas(dimensoes, corpo_grande)
    assert len(frutas_3) == 3

def test_fruta_nao_pode_nascer_dentro_da_cobra():
    dimensoes = (2, 2)
    corpo = [(0,0), (0,1), (1,0)]
    
    frutas = snake_funcs.gerar_frutas(dimensoes, corpo)
    
    assert frutas[0] == (1, 1)
    assert frutas[0] not in corpo
    

#Etapa 5 - Sistema de Colisão
def test_colisao_apenas_com_corpo():
    corpo_mordido = [(5,5), (6,5), (5,5)]
    assert snake_funcs.colisao(corpo_mordido) == True

    corpo_seguro = [(10,5), (9,5), (8,5)]
    assert snake_funcs.colisao(corpo_seguro) == False

#Etapa 6 - Regras de Progressão


#Etapa 7 - Atravessar Paredes
