# lista de grupos
grupos = [
    {
        "nome": "grupo 1",
        "herois": "h1=aquaman, dr_estranho, tor, ",
        "historia": "texto 1: "
    },
    {
        "nome": "grupo 2",
        "herois": "h2",
        "historia": "texto 2: "
    },
    {
        "nome": "grupo 3",
        "herois": "h3",
        "historia": "texto 3: "
    }
]
grupo_selecionado = {}
grupo_resp = input("digite_o_numero_de_um_grupo: ")
for temp_grupo in grupos:
    if temp_grupo["nome"] == grupo_resp:
        grupo_selecionado= temp_grupo
if grupo_selecionado["nome"]:
    print (grupo_selecionado["nome"])