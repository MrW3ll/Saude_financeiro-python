import json
import pandas as pd


def menu():
    pass

def salvar_transacoes(transacoes):
    with open('dados_financeiros.json','w') as f:
        json.dump(transacoes,f)


def carregar_transacoes():
    try:
        with open('dados_financeiros.json','r') as f:
            dados = json.load(f)
            return dados
    except FileNotFoundError:
        return []


def adicionar_transacao():
    transacoes = carregar_transacoes()

    while True:
        tipo = input('Qual tipo da transação? (receita/despesa)\n')
        data = input('Qual a data da transação? (dd/mm/aaaa)\n')
        descricao = input('Qual a descrição da transação?\n')
        valor = float(input('Qual o valor da transação?\n'))
        categoria = input('Qual a categoria da transação?\n')

        transacoes.append({
            'tipo':tipo,
            'data':data,
            'descricao':descricao,
            'valor':valor,
            'categoria':categoria,
        })

        continuar = input('Deseja adicionar outra transação? (s/n)\n')

        if continuar.lower() != 's':
            break
    
    salvar_transacoes(transacoes)
    print('Transações salvas com sucesso!')


def gerar_relatorio():
    dados = carregar_transacoes()

    if not dados:
        print('Nenhuma transação encontrada.')
        return    


    dados = pd.DataFrame(dados)
    dados['valor'] = dados['valor'].map(lambda x: f'R${x:.2f}')
    dados['tipo'] = dados['tipo'].str.capitalize()
    dados['categoria'] = dados['categoria'].str.capitalize()
    dados.columns = ['Tipo','Data', 'Descrição', 'Valor', 'Categoria']
    return dados
    

    


