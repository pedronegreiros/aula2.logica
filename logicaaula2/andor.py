# num = int(input("digite um numero: "))

# if num >= 0 and num <= 10:
#     print("numero valido")
# else:
#     print("numero invalido")

# alternativa = str(input("voçê dejesa sair?: s/n")).lower()

# if alternativa == "s" or alternativa == "n":
#     print("operação valida")
#     if alternativa == "s":
#         print("adeus!")
#     else:
#         print("continue usando o programa")
# else:
#     print('operação invalida')

cor1 = str(input("digite uma cor: ")).lower().strip()
#O .lower serve para deixartudo que o usuario digitar em minusculo, para que o codigo seja processado idependente da letra sendo maiuscula ou minuscula

match cor1: 
    case "vermelha":
        print("pare")
    case "verde":
        print("avançe")
    case "amarelo":
        print("se acalme")
    case _:
        print("cor invalida")




