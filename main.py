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

"""
PRINCIPAIS OBJETIVOS:
✔ eliminar redundância
✔ corrigir lógica conceitual
✔ deixar funções previsíveis
✔ preparar para próxima análise

"""



## calcula de valores
def calcular_total_receitas(valores): ##calcula a soma total de valores | Receitas
    total_valores = sum(item['valor'] for item in valores)  
    return total_valores

def calcular_total_despesas(valores): ##calcula a soma total de valores | Despesas
    total_valores = sum(item['valor'] for item in valores)  
    return total_valores


def saldo_final(receitas, despesas):  ##calcula o saldo final 
    return calcular_total_receitas(receitas) - calcular_total_despesas(despesas) 


def renda_comprometida(despesas, receitas): ## retorna quanto da renda (receitas) esta comprometida
    total_despesas = calcular_total_despesas(despesas)
    total_receitas = calcular_total_receitas(receitas)
    
    if total_receitas == 0:
        return 0
    
    return (total_despesas / total_receitas) * 100


## retornos
print(f'Total de receitas:R${calcular_total_receitas(receitas):.2f}')
print(f'Total de despesas:R${calcular_total_despesas(despesas):.2f}')
print(f'Saldo final: R${saldo_final(receitas,despesas):.2f}')
print(f'Sua renda esta comprometida em {renda_comprometida(despesas,receitas):.2f}%')