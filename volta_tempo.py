opcoes = {
    "SIM": "rebobina o tempo",
    "NÃO": "A missão fracassou",

}

status = "AGUARDANDO"



while ( status == "AGUARDANDO" ):
  opcao = input ("Você permite que Doutor Estranho volte no tempo?: ")
  if ( opcao != "SIM" ):
    print("Missão fracassou, o navio foi destruido")
    status = "FINALIZADO"
  else:
    print("Permissão Concedida! Doutor Estranho irá rebobinar o tempo: ")

    for chave, valor in opcoes.items():
      (chave + " = " + valor )

    opcao = input("Digite CONFIRMAR para reiniciar a missão: ")

    if ( opcao != "CONFIRMAR"):
      if(opcao in opcoes):
        print("Você escolheu " + opcoes[opcao])
        
      else:
        print("A missão fracassou")
        status= "FINALIZADO"
