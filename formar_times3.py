import random
def sorteio_de_times(n):
    #print(n)
    qtsDeJogadores = 2
    jogadorSort = random.randint(0, qtsDeJogadores-1)
    time1.append(n[jogadorSort])
    time2.append(n[1-jogadorSort])

def sorteio_sup(n):
    qtdSup = len(n)
    jogadorSort = random.randint(0, qtdSup-1)
    time1.append(n[jogadorSort])
    if (jogadorSort == 0):
        jogadorSort = random.randint(0, qtdSup-2)
        time2.append(n[jogadorSort+1])
    else:
        time2.append(n[0])

def consertar():
    if(time1[4]==sup[0]):
        duplicado = time2[4]
    else:
        duplicado = time1[4]
    for i in range(4):
        if (time1[i] == duplicado):
            time1[i] = 'Just Follow Me'
            break
        if (time2[i] == duplicado):
            time2[i] = 'Just Follow Me'
            break
time1=[]
time2=[]

jg = ['LeoBardo','huey']
top = ['jpsuperdrive','Ognarf']
mid =['Rayquaza de boné','pedrogois']
adc = ['GameCah','BeMyLewski']
sup = ['poc suporte','Ognarf','BeMyLewski','pedrogois']

sorteio_de_times(top)
sorteio_de_times(jg)
sorteio_de_times(mid)
sorteio_de_times(adc)
sorteio_sup(sup)
consertar()
print("Time 1:",time1,"\nTime 2:",time2)