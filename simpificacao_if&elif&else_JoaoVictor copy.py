preco_frutas = {

    'maçã': 2.5,
    'banana': 1.8,
    'laranja': 3.0

}

fruta_desejada = 'maçã'

resultado = preco_frutas.get(fruta_desejada, 'fruta não encontrada')

print(f"O preço da {fruta_desejada} é R${resultado}")