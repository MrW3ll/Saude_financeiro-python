## Estrutura inicial do código para controle financeiro ##
## Dados DUMMY's ##
receitas = [
    {'descricao':'Salário','valor':5000}
]

despesas = [
    {'descricao':'Aluguel','valor':900,'categoria':'moradia'},
    {'descricao':'cinema','valor':150,'categoria':'lazer'},
    {'descricao':'mercado','valor':800,'categoria':'alimentacao'},
    {'descricao':'gasolina','valor':100,'categoria':'transporte'}
]

"""
PRINCIPAIS OBJETIVOS:
✔ eliminar redundância
✔ corrigir lógica conceitual
✔ deixar funções previsíveis
✔ preparar para próxima análise

Issues:
2 - Total Receita
3 - Total despesas
4 - Saldo final
5 -  Ocupacao de renda

"""


def calcular_valores(valores):
    return sum(item['valor'] for item in valores)


def saldo_final():
    receita = calcular_valores(receitas)
    despesa = calcular_valores(despesas)
    return receita - despesa

def ocupacao_receita():
    if calcular_valores(receitas) > 0:
        return (calcular_valores(despesas) / calcular_valores(receitas)) * 100
    else:
        return 0
    

print(calcular_valores(despesas))