ligado = 1
opcao = 0
itens = []
entrada = 0

while ligado == 1:
  print("\n--------------------\nLista:", itens, "\n--------------------")
  print("\nMENU\nEscolha uma tarefa:\n1. Inserir elemento\n2. Remover elemento\n3. Desligar")
  opcao = int(input("= "))

  match opcao:
    case 1:
      entrada = input("\nInsira um elemento: ")
      itens.append(entrada)
    case 2:
      entrada = input("\nRemova um elemento: ")
      if entrada in itens:
        itens.remove(entrada)
      else:
        print("\nErro: A lista não contém este elemento.")
    case 3:
      ligado = 0

print("\nPrograma finalizado.")