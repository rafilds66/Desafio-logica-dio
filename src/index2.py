def determinaNivel(xp):
    intervalo = {
        (0, 1000): "Ferro",
        (1001, 2000): "Bronze",
        (2001, 5000): "Prata",
        (5001, 7000): "Ouro",
        (7001, 8000): "Platina",
        (8001, 9000): "Ascendente",
        (9001, float('inf')): "Imortal",
    }
    
    for intervalo, nivel in intervalo.items():
        if intervalo[0] <= xp <= intervalo[1]:
            return nivel
    
    return "Radiante" 

nomeHeroi = input("Digite o nome do seu Herói: ")
xpHeroi = int(input("Digite o XP do seu Herói: "))

nivelHeroi = determinaNivel(xpHeroi)

print("O Herói {} possui {} de XP e está no Nível {}." .format(nomeHeroi, xpHeroi, nivelHeroi ))
