import random
def sorteio_de_times(n):
    #print(n)
    qtsDeJogadores = len(n)
    while True:
        jogadorSort = random.randint(0, qtsDeJogadores-1)
        jogador1 = n[jogadorSort]
        if(jogador1 not in usados):
            time1.append(jogador1)
            usados.append(jogador1)
            break
    while True:

        jogadorSort = random.randint(0, qtsDeJogadores-1)
        jogador2 = n[jogadorSort]
        if(jogador2 not in usados):
            time2.append(jogador2)
            usados.append(jogador2)
            break
    
usados = []
time1=[]
time2=[]

jg = ['LeoBardo','huey']
top = ['jpsuperdrive','Just Follow me']
mid =['Rayquaza de boné','pedrogois']
adc = ['GameCah','BeMyLewski']
sup = ['poc suporte','Ognarf']

sorteio_de_times(top)
sorteio_de_times(jg)
sorteio_de_times(mid)
sorteio_de_times(adc)
sorteio_de_times(sup)
print("Time 1:",time1,"\nTime 2:",time2)