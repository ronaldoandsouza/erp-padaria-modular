import json
import os

ARQUIVO_ESTOQUE = 'estoque_insumos.json'
ARQUIVO_LOG = 'historico_vendas_detalhado.txt'

def carrgar_estoque_do_disco():
    if not os.path.exists(ARQUIVO_ESTOQUE):
        return {'mussarela': 5000, 'presunto': 5000, 'pao_frances': 50, 'tomate': 2000}
    with open(ARQUIVO_ESTOQUE, "r", encoding="utf-8") as f:
        return json.load(f)
    
def salvar_estoque_no_disco(estoque):
    with open(ARQUIVO_ESTOQUE, "w", encoding="utf-8") as f:
        json.dump(estoque, f, indent=4)

def gravar_linha_log(mensagem):
    with open(ARQUIVO_LOG, "a", encoding="utf-8") as f:
        f.write(mensagem + '\n')
