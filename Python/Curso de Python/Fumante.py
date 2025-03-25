cigarros_por_dia = int(input('Quantos cigarros você fuma por dia? '))
anos_fumando = int(input('Há quantos anos você fuma? '))

# Calcula o total de cigarros fumados ao longo dos anos
total_cigarros_fumados = cigarros_por_dia * (anos_fumando * 365)

# Cada cigarro reduz a vida em 10 minutos
minutos_perdidos = total_cigarros_fumados * 10

# Converte minutos perdidos para dias
dias_de_vida_perdidos = minutos_perdidos / (60 * 24)

print(f"Você perdeu aproximadamente {dias_de_vida_perdidos:.2f} dias de vida devido ao fumo.")
