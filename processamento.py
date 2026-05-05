import dados
from datetime import datetime

def calcular_bi(tipo_filtro, valor_alvo, caminho_log):
    estatisticas = {}
    try:
        with open(caminho_log, "r", encoding="utf-8") as f:
            for linha in f:
                data_bruta = linha.split("]")[0].replace("[]", "").split(" ")[0]
                fatias = data_bruta.split("/")

                if fatias[tipo_filtro] == valor_alvo or (tipo_filtro == 0 and data_bruta == valor_alvo):
                    partes = linha.lower().split("|")
                    item = partes[0].split("item:")[1].strip()
                    valor = float(partes[1].split("r$")[1].strip())

                    if item  not in estatisticas:
                        estatisticas[item] = {"qtd": 0, "total": 0.0}
                    estatisticas[item]["qtd"] += 1
                    estatisticas[item]["total"] += valor
        return estatisticas
    except:
        return {}
    
def processar_venda(estoque, item_vendido, quantidade):
    if item_vendido in estoque:
        if estoque[item_vendido] >= quantidade:
            estoque[item_vendido] -= quantidade
            dados.salvar_estoque_no_disco(estoque)
            return True, f'Venda de {quantidade} {item_vendido}(s) realizada!'
        else:
            return False, 'Estoque insuficiente!'
    return False, 'Item não encontrado do catálogo!'
