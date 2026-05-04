import dados
import processamento
import interface
from datetime import datetime

def rodar_sistema():
    # Inicialização
    estoque = dados.carrgar_estoque_do_disco()
    saldo_caixa = 0.0
    cargo_usuario = 'ADMIN' # Simulando login direto para testar

    while True:
        opcao = interface.exibir_menu_principal(cargo_usuario, saldo_caixa)

        if opcao == "1":
            # Lógica rápida de venda para teste
            item = 'bauru'
            valor = 14.00
            # 1. Registra no log via módulo de DADOS
            data_hora = datetime.now().strftime("%d/%m/%y %H:%M:%S")
            linha = f'[{data_hora}] item: {item} | R$ {valor}'
            dados.gravar_linha_log(linha)

            # 2. Atualiza saldo
            saldo_caixa += valor
            print(f'\nVenda de {item} realizada!')
            input('Enter...')

        elif opcao == "3":
            # Usando o módulo de PROCESSAMENTO para o BI
            mes = input('Digite o mês para o relatório (ex: 05): ')
            # Chamamos a função que está em outro arquivo!
            resultado = processamento.calcular_bi(1, mes, dados.ARQUIVO_LOG)
            interface.exibir_relatorio(resultado, f'Relatório do Mês {mes}')

        elif opcao == "0":
            print('Fechando sistema... Até amanhã!')
            break


if __name__ == '__main__':
    rodar_sistema()