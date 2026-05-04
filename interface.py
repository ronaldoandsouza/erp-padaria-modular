import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def exibir_menu_principal(cargo, saldo):
    limpar_tela()
    print('=== ERP PADARIA PRO v4.0 ===')
    print(f'SESSÃO: {cargo} | SALDO EM CAIXA: R$ {saldo:.2f}')
    print('-'*35)
    print('1. Nova Venda')
    print('2. Consultar Estoque')
    print('3. Painel de BI (Relatórios)')
    print('0. sair')
    return input('\nEscolha uma opção: ')

def exibir_relatorio(dados, titulo):
    limpar_tela()
    print(f'=== {titulo.upper()} ===')
    if not dados:
        print('Nenhum registro encontrado.')
    else:
        for item, info in dados.items():
            print(f'{item.capitalize():<15} | Qtd: {info["qtd"]:>3} | Total: R$ {info["total"]:>8.2f}')
    input('\nPressione Enter para voltar...')