from pathlib import Path

Dir = input("URL da pasta a ser organizada: ")
diretorio = Path(Dir)

pastas = {
    ".pdf": diretorio / "Arquivos PDF",
    ".zip": diretorio / "Compactados",
    ".exe": diretorio / "Executáveis",
    ".png": diretorio / "Fotos",
    ".jpg": diretorio / "Fotos",
    '.mp4':diretorio/ "Videos"
}  # dicionário para economizar linhas
for pasta in pastas.values():  # criação das pastas
    pasta.suffix.lower()
    if not pasta.exists():
        pasta.mkdir(parents=True, exist_ok=True)


for item in diretorio.iterdir():
    sufixo = item.suffix.lower()
    if sufixo in pastas:
        destino = pastas[sufixo] / item.name
        item.rename(destino) #move o arquivo
        
print('Prontinho! :)')
