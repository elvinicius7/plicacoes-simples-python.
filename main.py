tarefas = []

def listar():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    for i, t in enumerate(tarefas, start=1):
        print(f"{i}. {t}")

while True:
    print("\n1 - Adicionar | 2 - Listar | 0 - Sair")
    op = input("Escolha: ")
    if op == "1":
        tarefas.append(input("Digite a tarefa: "))
    elif op == "2":
        listar()
    elif op == "0":
        break
    else:
        print("Opção inválida")
