## Estrutura inicial do código para controle financeiro ##
## Dados DUMMY's ##
receitas = [
    {'descricao':'Salário','valor':5000},
    {'descricao':'Freelance','valor':1500}
]

despesas = [
    {'descricao':'Aluguel','valor':1200,'categoria':'Moradia'},
    {'descricao':'Supermercado','valor':800,'categoria':'Alimentação'},
    {'descricao':'Transporte','valor':300,'categoria':'Transporte'},
    {'descricao':'Cinema','valor':200,'categoria':'Lazer'}
]

## Calcular receita total ## 
def calcular_total_receitas(receitas):
    total_receita = sum(item['valor'] for item in receitas)
    return total_receita

print(f'Total de receitas:R${calcular_total_receitas(receitas):.2f}')

