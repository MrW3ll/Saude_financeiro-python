import json
import pandas as pd


def menu():
    print(f'1 - Gerar extrato de movimentações \n'
        '2 - Adicionar movimentações \n'
        '3 - Editar movimentações \n' ## Função ainda não criada
        '4 - Apagar movimentações \n' ## Função ainda não criada
        
        )
    
    opcao = input('Informe a opção desejada: \n')

    

    match opcao:
        case 1:
            carregar_transacoes()
        case 2:
            adicionar_transacao()


        case _:
            print(f'Opção informada invalida! Favor verificar')    



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
    dados = dados.sort_values(by='Data',ascending=False)
    print(dados)
    
def apagar_movimentacao():
    pass

def editar_movimentacao():
    pass

gerar_relatorio()
    


