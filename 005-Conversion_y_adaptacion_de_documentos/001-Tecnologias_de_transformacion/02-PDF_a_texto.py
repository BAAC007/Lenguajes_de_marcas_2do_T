#sudo apt install pypdf --break-system-packages
from pypdf import PDFreader

lector = PDFreader("librophp.pdf")
texto = ""

for pagina in lector.pages:
    texto += pagina.extract_text() + "\n"

print(texto)