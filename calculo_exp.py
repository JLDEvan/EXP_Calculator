'''
Calculo de experiencia para meu RPG
lvl 1 máx 15 -> lvl 2 máx 30 -> lvl 3 máx 45 . . .
**Importante compreender que:**
O EXP nunca é zerado, quando você passa para nível 2  você possuí um total de 15 de exp e 
a meta que você tem que alcançar para o nível 3 são mais 30 de EXP. Ou seja, no final você ficará com 45 de EXP e
faltarão mais 45 para alcançar o nível 4.
'''

def calcular_nivel(exp_total):
    nivel = 1
    exp_para_nivel_atual = 0
    exp_para_proximo_nivel = 15

    while exp_total >= exp_para_nivel_atual + exp_para_proximo_nivel:
        exp_para_nivel_atual += exp_para_proximo_nivel
        exp_para_proximo_nivel += 15
        nivel += 1

    exp_restante_para_proximo_nivel = exp_para_nivel_atual + exp_para_proximo_nivel - exp_total
    return nivel, exp_restante_para_proximo_nivel

exp_total = 0
nivel_atual, exp_faltando = calcular_nivel(exp_total)

print(f"Seu personagem está no nível {nivel_atual}.")
print(f"Faltam {exp_faltando} de EXP para alcançar o próximo nível.")