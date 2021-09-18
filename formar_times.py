import random
time1 = []
time2 = []
#sorteando top time1
jogadoresTop = ['jpsuperdrive','rayquaza de boné','Ognarf','huey']
print(jogadoresTop)
qtsTopLaners = len(jogadoresTop)
jogadorSort = random.randint(0, qtsTopLaners-1)
time1.append(jogadoresTop[jogadorSort])
jogadoresTop.remove(jogadoresTop[jogadorSort])

#sorteando top time2
qtsTopLaners = len(jogadoresTop)
jogadorSort = random.randint(0, qtsTopLaners-1)
time2.append(jogadoresTop[jogadorSort])
jogadoresTop.remove(jogadoresTop[jogadorSort])

#sorteando o jg time 1
jogadoresJG = ['LeoBardo','huey']
print(jogadoresJG)
qtsJungles = len(jogadoresJG)
jogadorSort = random.randint(0, qtsJungles-1)
time1.append(jogadoresJG[jogadorSort])
jogadoresJG.remove(jogadoresJG[jogadorSort])

#sorteando JG time2
qtsJungles = len(jogadoresJG)
jogadorSort = random.randint(0, qtsJungles-1)
time2.append(jogadoresJG[jogadorSort])
jogadoresJG.remove(jogadoresJG[jogadorSort])

#sorteando o MID time 1
jogadoresMid = ['rayquaza de boné','ConanStyle','Pedro Góis']
print(jogadoresMid)
qtsMids = len(jogadoresMid)
jogadorSort = random.randint(0, qtsMids-1)
time1.append(jogadoresMid[jogadorSort])
jogadoresMid.remove(jogadoresMid[jogadorSort])

#sorteando MID time2
qtsMids = len(jogadoresMid)
jogadorSort = random.randint(0, qtsMids-1)
time2.append(jogadoresMid[jogadorSort])
jogadoresMid.remove(jogadoresMid[jogadorSort])

#sorteando o ADC time 1
jogadoresAdc = ['gamecah','ConanStyle','BeMyLewski']
print(jogadoresAdc)
qtsAdcs = len(jogadoresAdc)
jogadorSort = random.randint(0, qtsAdcs-1)
time1.append(jogadoresAdc[jogadorSort])
jogadoresAdc.remove(jogadoresAdc[jogadorSort])

#sorteando ADC time2
qtsAdcs = len(jogadoresAdc)
jogadorSort = random.randint(0, qtsAdcs-1)
time2.append(jogadoresAdc[jogadorSort])
jogadoresAdc.remove(jogadoresAdc[jogadorSort])

#sorteando o SUP time 1
jogadoresSup = ['Leo Bardo','LPC','Ognarf','jpsuperdrive','Pedro Góis','gamecah']
print(jogadoresSup)
qtsSups = len(jogadoresSup)
jogadorSort = random.randint(0, qtsSups-1)
time1.append(jogadoresSup[jogadorSort])
jogadoresSup.remove(jogadoresSup[jogadorSort])

#sorteando SUP time2
qtsSups = len(jogadoresSup)
jogadorSort = random.randint(0, qtsSups-1)
time2.append(jogadoresSup[jogadorSort])
jogadoresSup.remove(jogadoresSup[jogadorSort])

print("Time 1:",time1)
print("Time 2:",time2)
