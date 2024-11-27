class Cadastro_livro:
    def __init__(self, nome_livro, autor, status):
        self.nome_livro = nome_livro
        self.autor = autor
        self._status = status = True


    def status_livro(self):
        if not self._status:
            return f"O livro {self.nome_livro} não está disponivel"
        else:
            return f"O livro {self.nome_livro} está indisponível"


class Usuario:
    def __init__(self, nome_usuario, idade, numero_livro, status):
        super.__init__(self, status)
        self.nome_usuario = nome_usuario
        self._numero_livro = numero_livro
        self.status = status
        self.idade = idade

    def emprestar_livro(self):
        if self.status():
            self._livro.apped(self._livro)
            return f"O livro {self._livro} foi emprestado"
        else:
            return f"O livro{self._livro} não pode ser emprestado"
            
    def devolver_livro(self):
        if not self.status:
            self._livro.pop(self._livro)
            return f"Livro {self._livro} foi devolvido"
        else:
            return f"Livro {self._livro} não foi devolvido"

class Admim:
    def __init__(self, nome_admim, idade):
        super.__init__(self, nome_admim, idade)
        

class Biblioteca:
     def __init__(self, status, nome_livro):
         self.status = status
         self.nome_livro = nome_livro
         super.__init__(self, status)
        
          

     def listar_livros(self):
        print("Livros disponíveis na biblioteca:")
        for livro in self.nome_livro:
            livro = "Disponível" if self.status() else "Emprestado"
            print(f"O livro {self.nome_livro} está {self.status}")


livro1 = Cadastro_livro("Pqueno principe", "Dôdo Pressão", "Disponivel")
livro1 = Cadastro_livro("grande principe", "Duda Olanda", "Disponivel")


aluno1 = Usuario("Carlos", "25", "251",)
admim1 = Admim("Sérgio", "45")

Biblioteca.listar_livros()

Usuario.emprestar_livro()
Usuario.devolver_livro()