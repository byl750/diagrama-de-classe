class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, matricula: str):
        super().__init__(nome, idade)
        self.matricula = matricula

    def estudar(self):
        print(f"{self.nome} está estudando.")


class Professor(Pessoa):
    def __init__(self, nome: str, idade: int, especialidade: str):
        super().__init__(nome, idade)
        self.especialidade = especialidade

    def lecionar(self):
        print(f"{self.nome} está lecionando {self.especialidade}.")


class Disciplina:
    def __init__(self, nome: str, professor: Professor):
        self.nome = nome
        self.professor = professor
        self.alunos = []

    def adicionar_aluno(self, aluno: Aluno):
        self.alunos.append(aluno)

    def listar_participantes(self):
        print(f"Disciplina: {self.nome}")
        print(f"Professor: {self.professor.nome}")
        print("Alunos:")
        for aluno in self.alunos:
            print(f"- {aluno.nome} ({aluno.matricula})")


# Exemplo de uso
prof = Professor("Carlos", 45, "Matemática")
aluno1 = Aluno("Ana", 16, "A001")
aluno2 = Aluno("Bruno", 17, "A002")

disciplina = Disciplina("Matemática", prof)
disciplina.adicionar_aluno(aluno1)
disciplina.adicionar_aluno(aluno2)

disciplina.listar_participantes()
