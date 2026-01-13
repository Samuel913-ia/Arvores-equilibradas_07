# ==============================
# SISTEMA DE CADASTRO COM AVL
# ==============================

# ---------- NÓ DA AVL ----------
class NoAVL:
    def __init__(self, matricula, nome, curso):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        self.esq = None
        self.dir = None
        self.altura = 1


# ---------- FUNÇÕES AUXILIARES ----------
def altura(no):
    if not no:
        return 0
    return no.altura


def fator_balanceamento(no):
    if not no:
        return 0
    return altura(no.esq) - altura(no.dir)


# ---------- ROTAÇÕES ----------
def rotacao_direita(y):
    x = y.esq
    T2 = x.dir

    x.dir = y
    y.esq = T2

    y.altura = 1 + max(altura(y.esq), altura(y.dir))
    x.altura = 1 + max(altura(x.esq), altura(x.dir))

    return x


def rotacao_esquerda(x):
    y = x.dir
    T2 = y.esq

    y.esq = x
    x.dir = T2

    x.altura = 1 + max(altura(x.esq), altura(x.dir))
    y.altura = 1 + max(altura(y.esq), altura(y.dir))

    return y


# ---------- INSERÇÃO NA AVL ----------
def inserir(no, matricula, nome, curso):

    if not no:
        return NoAVL(matricula, nome, curso)

    if matricula < no.matricula:
        no.esq = inserir(no.esq, matricula, nome, curso)
    elif matricula > no.matricula:
        no.dir = inserir(no.dir, matricula, nome, curso)
    else:
        return no  # não permite matrícula duplicada

    no.altura = 1 + max(altura(no.esq), altura(no.dir))
    fb = fator_balanceamento(no)

    # Caso LL
    if fb > 1 and matricula < no.esq.matricula:
        return rotacao_direita(no)

    # Caso RR
    if fb < -1 and matricula > no.dir.matricula:
        return rotacao_esquerda(no)

    # Caso LR
    if fb > 1 and matricula > no.esq.matricula:
        no.esq = rotacao_esquerda(no.esq)
        return rotacao_direita(no)

    # Caso RL
    if fb < -1 and matricula < no.dir.matricula:
        no.dir = rotacao_direita(no.dir)
        return rotacao_esquerda(no)

    return no


# ---------- BUSCA ----------
def buscar(no, matricula):
    if not no:
        return None

    if matricula == no.matricula:
        return no
    elif matricula < no.matricula:
        return buscar(no.esq, matricula)
    else:
        return buscar(no.dir, matricula)


# ---------- LISTAGEM EM ORDEM ----------
def listar_em_ordem(no):
    if no:
        listar_em_ordem(no.esq)
        print(f"Matrícula: {no.matricula} | Nome: {no.nome} | Curso: {no.curso}")
        listar_em_ordem(no.dir)


# ---------- MENU PRINCIPAL ----------
raiz = None

while True:
    print("\n===== SISTEMA DE CADASTRO (AVL) =====")
    print("1 - Cadastrar estudante")
    print("2 - Buscar estudante")
    print("3 - Listar estudantes")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        m = int(input("Matrícula: "))
        n = input("Nome: ")
        c = input("Curso: ")
        raiz = inserir(raiz, m, n, c)
        print("Estudante cadastrado com sucesso!")

    elif opcao == "2":
        m = int(input("Matrícula para buscar: "))
        est = buscar(raiz, m)
        if est:
            print(f"Encontrado -> Nome: {est.nome} | Curso: {est.curso}")
        else:
            print("Estudante não encontrado.")

    elif opcao == "3":
        print("\n--- LISTA DE ESTUDANTES ---")
        listar_em_ordem(raiz)

    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")
