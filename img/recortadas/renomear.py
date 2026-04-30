import os
import unicodedata

def remover_acentos(texto):
    # Separa os caracteres base dos acentos
    texto_normalizado = unicodedata.normalize('NFD', texto)
    # Filtra e remove os acentos (categoria 'Mn' = Mark, Nonspacing)
    return ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')

# Caminho da sua pasta
caminho = r"C:\Alx\afilosofiaeacidade\img"

# Lista todos os arquivos na pasta
for nome_arquivo in os.listdir(caminho):
    if nome_arquivo.lower().endswith(".png"):
        # 1. Remove os acentos
        novo_nome = remover_acentos(nome_arquivo)
        # 2. Troca os espaços por underline
        novo_nome = novo_nome.replace(" ", "_")
        
        # Só renomeia se o nome realmente precisar ser alterado
        if nome_arquivo != novo_nome:
            caminho_antigo = os.path.join(caminho, nome_arquivo)
            caminho_novo = os.path.join(caminho, novo_nome)
            
            os.rename(caminho_antigo, caminho_novo)
            print(f"Renomeado: '{nome_arquivo}' -> '{novo_nome}'")

print("Concluído!")