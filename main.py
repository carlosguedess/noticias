class Noticia:

    def __init__ (self, manchete, data_hora, lugar):

        self.manchete = manchete
        self.data_hora = data_hora
        self.lugar = lugar

    def exibir_informações(self):
        print(f"Manchte de: {self.manchete}, data e hora: {self.data_hora} lugar: {self.lugar}")

Noticia1 = Noticia
Noticia.exibir_informações()
print(Noticia)