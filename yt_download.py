#customtkinter = a interface utilizada no projeto
import customtkinter
from pytube import YouTube
# utilizado caixas de diálogo de arquivo ajudam você a abrir, salvar arquivos ou diretórios.
from tkinter import filedialog

# Configuração da interface
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Função para baixar o vídeo
def download_youtube_video():
    video_url = url.get()
    download_path = caminho.get()
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(download_path)
        print("Download completo!")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar baixar o vídeo: {e}")

# Função para selecionar a pasta de destino
def escolher_pasta_destino():
    pasta_selecionada = filedialog.askdirectory()
    if pasta_selecionada:
        caminho.delete(0, customtkinter.END)
        caminho.insert(0, pasta_selecionada)

# Criação da janela principal
janela = customtkinter.CTk()
janela.geometry("500x300")

texto = customtkinter.CTkLabel(janela, text="Aplicativo para baixar vídeos do YouTube")
texto.pack(padx=10, pady=10)

url = customtkinter.CTkEntry(janela, placeholder_text="A url do vídeo")
url.pack(padx=10, pady=10)

caminho = customtkinter.CTkEntry(janela, placeholder_text="Pasta destino")
caminho.pack(padx=10, pady=10)

botao_escolher_pasta = customtkinter.CTkButton(janela, text="Escolher Pasta", command=escolher_pasta_destino)
botao_escolher_pasta.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Baixar", command=download_youtube_video)
botao.pack(padx=10, pady=10)

janela.mainloop()