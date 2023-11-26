nomeHeroi = input("Digite o nome do seu Herói: ")
xpHeroi = int(input("Digite o Xp do seu herói: "))
nivelHeroi = " "

if xpHeroi < 1000:
    nivelHeroi = "Ferro"
    print("O Herói {} possui {} de XP e está no Nível {}." .format(nomeHeroi, xpHeroi, nivelHeroi))
    
elif xpHeroi > 1000 and xpHeroi <= 2000:
    nivelHeroi = "Bronze"
    print("O Herói {} possui {} de XP e está no Nível {}." .format(nomeHeroi, xpHeroi, nivelHeroi))
    
elif xpHeroi > 2000 and xpHeroi <= 5000:
    nivelHeroi = "Prata"
    print("O Herói {} possui {} de XP e está no Nível {}." .format(nomeHeroi, xpHeroi, nivelHeroi))

elif xpHeroi > 5000 and xpHeroi <= 7000:
    nivelHeroi = "Ouro"
    print("O Herói {} possui {} de XP e está no Nível {}." .format(nomeHeroi, xpHeroi, nivelHeroi))
    
elif xpHeroi > 7000 and xpHeroi <= 8000:
    nivelHeroi = "Platina"
    print("O Herói {} possui {} de XP e está no Nível {}." .format(nomeHeroi, xpHeroi, nivelHeroi))

elif xpHeroi > 8000 and xpHeroi <= 9000:
    nivelHeroi = "Ascendente"
    print("O Herói {} possui {} de XP e está no Nível {}." .format(nomeHeroi, xpHeroi, nivelHeroi))
    
elif xpHeroi > 9000 and xpHeroi <= 1000:
    nivelHeroi = "Imortal"
    print("O Herói {} possui {} de XP e está no Nível {}." .format(nomeHeroi, xpHeroi, nivelHeroi))
    
else:
    nivelHeroi = "Radiante"
    print("O Herói {} possui {} de XP e está no Nível {}." .format(nomeHeroi, xpHeroi, nivelHeroi))

    