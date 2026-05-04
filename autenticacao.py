import os

# Banco de dados simples de usuários
# Nível 1: Admin (Acesso total) | Nível 0: Caixa (Acesso restrito)
USUARIOS = {
    'ronaldo': {'senha': '789', 'nivel': 1},
    'caixa01': {'senha': '123', 'nivel': 0}
}

def realizar_login():
    os.system("cls" if os.name == "nt" else "clear")
    print('='*30)
    print(f'{"LOGIN DO SISTEMA":^30}')
    print('='*30)

    usuario = input('Usuário: ').lower().strip()
    senha = input('senha: ').strip()

    if usuario in USUARIOS and USUARIOS[usuario]['senha'] == senha:
        print(f'\n[OK] Bem-Vindo, {usuario.capitalize()}!')
        input('Pressione Enter para entrar...')
        return usuario, USUARIOS[usuario]['nivel']
    else:
        print('\n[ERRO] Usuário ou senha incorretos.')
        input('Tente novamente...')
        return None, None