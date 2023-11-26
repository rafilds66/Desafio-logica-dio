//Desafio Classificador de nível de Heroí

function determinaNivel(xp) {
    const intervalos = [
        { min: 0, max: 1000, nivel: "Ferro" },
        { min: 1001, max: 2000, nivel: "Bronze" },
        { min: 2001, max: 5000, nivel: "Prata" },
        { min: 5001, max: 7000, nivel: "Ouro" },
        { min: 7001, max: 8000, nivel: "Platina" },
        { min: 8001, max: 9000, nivel: "Ascendente" },
        { min: 9001, max: Infinity, nivel: "Imortal" }
    ];

    for (const intervalo of intervalos) {
        if (xp >= intervalo.min && xp <= intervalo.max) {
            return intervalo.nivel;
        }
    }

    return "Radiante";
}

const nomeHeroi = prompt("Digite o nome do seu Herói: ");
const xpHeroi = parseInt(prompt("Digite o XP do seu Herói:"));

const nivelHeroi = determinaNivel(xpHeroi);

console.log(`O Herói ${nomeHeroi} possui ${xpHeroi} de XP e está no Nível ${nivelHeroi}.`);

