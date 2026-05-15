import json
import pandas as pd
import keyboard


def menu():
    print(f'1 - Gerar extrato de movimentações \n'
        '2 - Adicionar movimentações \n'
        '3 - Editar movimentações \n' ## Função ainda não criada
        '4 - Apagar movimentações \n' ## Função ainda não criada
        'ESC - para encerrar'
        )
    
    while True:
        opcao = int(input('Informe a opção desejada: \n'))

        if keyboard.is_pressed('esc'):
            print(f'Encerrando programa')
            break


        match opcao:
            case 1:
                gerar_relatorio()
            case 2:
                adicionar_transacao()
            case 3:
                editar_movimentacao()
            case 4:
                apagar_movimentacao()    
            case _:
                print(f'Opção informada invalida! Favor verificar')    
                continue



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
        try:
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

            salvar_transacoes(transacoes)
            print(f'Transação salva com sucesso')
        except Exception as e:
            print(f'Erro ao salvar informações: {e}')

        continuar = input('Deseja adicionar outra transação? (s/n)\n')

        if continuar.lower() != 's':
            
            continuar = input(f'Retornar ao menu principal? (s/n)\n')
            if continuar.lower() == 'n':
                break
            else:
                continue       
    
    


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
    opcao = input('\nRetornar ao menu: (s/n)\n')
    if opcao != 's':
        print('MOMENTO DE ENCERRAR PROGRAMA - EM CONSTRUÇÃO')
    



def apagar_movimentacao():

    transsacoes = carregar_transacoes()

    while True:
        
        break

    pass

def editar_movimentacao():
    
    transacoes = carregar_transacoes()
    


    while True:
        
        break

    pass




menu()
    


