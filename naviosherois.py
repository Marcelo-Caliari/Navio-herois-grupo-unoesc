import random
print (random.randrange(0,11) )

resposta_permitido_atacar = input("deseja atacar?s/n")
is_permitido_atacar=False 
if(resposta_permitido_atacar == "s"): 
    is_permitido_atacar = True
    print("os heróis vão atacar")
if(resposta_permitido_atacar == "n"):
    print("os vilões vão atacar o navio")