#  pedir relatório
#  mostrar status (está encalhado e âlgulo do navio)
#  se estiver preso, desprender (deseja desprender navio)
#  três alternativas de ângulo e ter um angulo fixo para navio

pontuacao = 0
angulo_atual = 45
angulo_ideal = 180
is_navio_preso = True

print('Qual é o relatório da situação')
print('==================DADOS DO SCANNER====================')
print("Navio está preso: ", ("SIM" if is_navio_preso else "NÃO"))
print("Angulo em relação ao canal: ",
      angulo_atual, "º ideal(", angulo_ideal, "º)")
print('======================================================')

desprender_navio = ""
if (is_navio_preso):
    desprender_navio = input(
        "Deseja enviar forças para desprender o navio? (S/N): ")

is_navio_preso = not (desprender_navio == "S")

print('==================DADOS DO SCANNER====================')
print("Navio está preso: ", ("SIM" if is_navio_preso else "NÃO"))
print("Angulo em relação ao canal: ",
      angulo_atual, "º ideal(", angulo_ideal, "º)")
print('======================================================')

print("Você ainda precisa corrigir o angulo do navio para desencalhá-lo")
while angulo_atual != angulo_ideal:
    angulo_restante = int(input("Adicione quantos angulos faltam para o navio chegar ao angulo ideal:"))
    angulo_atual = angulo_atual + angulo_restante
    print('==================DADOS DO SCANNER====================')
    print("Navio está preso: ", ("SIM" if is_navio_preso else "NÃO"))
    print("Angulo em relação ao canal: ",
        angulo_atual, "º ideal(", angulo_ideal, "º)")
    print('======================================================')

pontuacao_navio_preso = 40 if not is_navio_preso else 0
pontuacao_angulo =  60 if angulo_atual == angulo_ideal else 0
pontuacao = pontuacao_navio_preso + pontuacao_angulo

if (pontuacao == 100):
    print("Parabens!")
else: 
    print("Que pena! Você combateu os vilões porem o navio ainda não foi desencalhado")

print('======================================================')
print("Sua pontuação foi ",pontuacao)
print('======================================================')
