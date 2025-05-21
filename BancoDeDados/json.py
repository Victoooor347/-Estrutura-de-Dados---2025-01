import json

# Dicionário
dados_python = {
    "nome": "João",
    "idade": 30,
    "cidade": "Vale Veneto",
    "interesses": ["programação", "música", "jogos"],
    "Matrucula ativa": True,
    "hobbies": None,
    "familia": {"Pai": "Pedro", "Mãe": "Maria"}
}

# Salvando o dicionário em um arquivo JSON
with open('dados.json', 'w', encoding='latin') as file:
    json.dump(dados_python, file, ensure_ascii=False, indent=4)

# Carregando o arquivo JSON e exibindo com formatação "pretty"
with open('dados.json', 'r', encoding='latin') as file:
    dados_carregados = json.load(file)
    print("Dados carregados do arquivo JSON:")
    print(json.dumps(dados_carregados, ensure_ascii=False, indent=4))

# Mostrar os dados como o python os ve:
print(dados_carregados) # None é null, True é true

dados_carregados["nome"]