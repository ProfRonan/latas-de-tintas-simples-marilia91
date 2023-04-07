print("Bem vindo à Loja de Tintas do seu ZÉ")
metros_quadrados = input("Qual a área em m²?\n")
metros_quadrados = float(metros_quadrados)

# Coloque o código para resolver o problema nessa parte do programa
qtd_de_latas = metros_quadrados / 54
valor_total = qtd_de_latas * 80

if metros_quadrados <= 54: 
  qtd_de_latas = 1
  valor_total = 80
  
elif metros_quadrados % 54 != 0:
  qtd_de_latas = int(qtd_de_latas) + 1
  valor_total = qtd_de_latas * 80

else: 
  qtd_de_latas = metros_quadrados / 54
  valor_total = qtd_de_latas * 80

#outra solução: 
#if qtd_de_latas == int(qtd_de_latas):
    #qtd_de_latas = int(qtd_de_latas)

#else:
    #qtd_de_latas = int(qtd_de_latas) +  1
    #valor_total = qtd_de_latas * 80
    

# As duas variáveis qtd_de_latas e valor_total devem guardar a resposta do problema
# Troque os zeros pelos valores corretos.
#qtd_de_latas = 0
#valor_total = 0

print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}")