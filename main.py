import dados
import processamento
import interface
import autenticacao  # Importamos seu novo módulo de segurança
from datetime import datetime

def rodar_sistema():
    # 1. Carregamento inicial
    estoque = dados.carregar_estoque_do_disco()
    saldo_sessao = 0.0
    
    usuario_logado = None
    nivel_acesso = None

    # 2. Loop de Autenticação (O sistema só passa daqui com senha correta)
    while usuario_logado is None:
        usuario_logado, nivel_acesso = autenticacao.realizar_login()

    # 3. Loop Principal do ERP
    while True:
        # Passamos o nome do usuário para a interface mostrar no topo
        opcao = interface.exibir_menu_principal(usuario_logado.upper(), saldo_sessao)

        if opcao == '1':
            # 1. Perguntar o que está vendendo
            item = input('Qual item foi vendido? (Ex: Pão Frances, bolo): ').strip()

            try:
                qtd = int(input(f'Quantidade de {item}: '))
                sucesso, mensagem = processamento.processar_venda(estoque, item, qtd)
                if sucesso:
                    print(f'\n[OK] {mensagem}')
                    saldo_sessao += (qtd * 0.50)
                else: 
                    print(f'\n[ERRO]: {mensagem}')
            
            except ValueError:
                print('\nDigite um número válido para a quantidade!')

            input('\nPressioneEnter para continuar')

        elif opcao == '2':
            # Consultar Estoque (Nível 0 e 1 podem ver)
            interface.exibir_relatorio(estoque, "Posição de Estoque")

        elif opcao == '3':
            # Painel de BI (APENAS NÍVEL 1 - ADMIN)
            if nivel_acesso >= 1:
                mes = input("Digite o mês (ex: 05): ")
                resultado = processamento.calcular_bi(1, mes, dados.ARQUIVO_LOG)
                interface.exibir_relatorio(resultado, f"BI - Mensal ({mes})")
            else:
                print("\n[ACESSO NEGADO] Você não tem permissão para ver relatórios financeiros.")
                input("Pressione Enter...")

        elif opcao == '0':
            print(f"\nSessão de {usuario_logado} encerrada. Saindo...")
            break

if __name__ == "__main__":
    rodar_sistema()