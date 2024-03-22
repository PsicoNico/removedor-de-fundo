from rembg import remove
from PIL import Image

imagem = Image.open("endereço da imagem aqui")

imagem_sem_fundo = remove(imagem)

imagem_sem_fundo.save("imagem_sem_fundo.png")