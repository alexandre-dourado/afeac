import os
from PIL import Image

def trim_images(input_folder, output_folder):
    # Cria a pasta de saída se não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.png'):
            path = os.path.join(input_folder, filename)
            
            with Image.open(path) as img:
                # Converte para RGBA para garantir que temos o canal alpha
                img = img.convert("RGBA")
                
                # getbbox() encontra as coordenadas do conteúdo (ignorando zeros/transparência)
                bbox = img.getbbox()
                
                if bbox:
                    # Recorta a imagem nas coordenadas encontradas
                    cropped_img = img.crop(bbox)
                    
                    # Salva na pasta de destino
                    save_path = os.path.join(output_folder, filename)
                    cropped_img.save(save_path)
                    print(f"Processado: {filename}")
                else:
                    print(f"Aviso: {filename} está totalmente vazia.")

# Configurações
pasta_origem = 'C:/Alx/afilosofiaeacidade/img/recortadas'
pasta_destino = 'C:/Alx/afilosofiaeacidade/img/recortadas'

trim_images(pasta_origem, pasta_destino)