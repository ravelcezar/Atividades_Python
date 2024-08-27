maca_12 = float(0.30)
maca_6 = float(0.25)

total_maca = int(input("Digite quantas maças você quer comprar: "))

if total_maca >= 12:
    valor_total = total_maca * maca_12
else:
    valor_total = total_maca * maca_6


print(f"O valor total da compra é R$ {valor_total:.2f}")