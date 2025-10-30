# Populações iniciais
pop_a = 80000
pop_b = 200000

# Taxas de crescimento
taxa_a = 0.03
taxa_b = 0.015

anos=0

while pop_a < pop_b:
    pop_a += pop_a * taxa_a
    pop_b += pop_b * taxa_b
    anos += 1

print(f"A população do pais A ultrapassará ou igualará a do pais b em {anos} anos.")