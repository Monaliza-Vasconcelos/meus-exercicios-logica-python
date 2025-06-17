quant_km_percorridos = float(input('Quantidade de km percorrido? '))
quant_dias_alugado = int(input('Quantidade de dias que o carro foi alugado? '))
km_rodados = quant_km_percorridos*0.20
dias = quant_dias_alugado * 90
preco_total_a_pagar = km_rodados + dias
print('Valor total a pagar: R${}'.format(preco_total_a_pagar))