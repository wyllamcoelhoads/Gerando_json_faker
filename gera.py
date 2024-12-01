#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from faker import Faker
import random

# Lista de algumas cidades brasileiras
cidades_brasileiras = [
    "Sao Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", 
    "Curitiba", "Salvador", "Recife", "Fortaleza", "Manaus", 
    "Brasilia", "Natal", "Joao Pessoa", "Goiania", "Vitoria", 
    "Florianopolis", "Campo Grande", "Maceio", "Cuiaba", "Aracaju", 
    "Belem", "Macapa", "Boa Vista", "Palmas", "Teresina", "Sao Luis", 
    "Campo Grande", "Aracaju"
]

tamanho = [
    75, 85, 65, 100, 63, 84, 96, 465, 82, 120, 235, 125 
]

tipoInteresse = [
    "Casa", "Apartamento", "Galpao", "Terreno"
]

fake = Faker('pt_BR')

# Caminho do arquivo de entrada e saída
input_file = 'registros.json'
output_file = 'novosregistros.json'

# Criar uma instância do Faker
fake = Faker()

try:
    # Carregar os dados do arquivo JSON
    with open(input_file, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    # Atualizar os endereços no JSON
    for pessoa in dados:
        pessoa['Nome'] = fake.name()
        pessoa['Email'] = fake.email()
        pessoa['Cidade'] = random.choice(cidades_brasileiras)
        pessoa['Tamanho'] = random.choice(tamanho)
        pessoa['TipoDeImoveInteresse'] = random.choice(tipoInteresse)


    # Salvar os dados modificados em um novo arquivo JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4)

    print(f"Os nomes foram atualizados e os dados foram salvos em '{output_file}'.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{input_file}' não foi encontrado.")
except json.JSONDecodeError:
    print(f"Erro: O arquivo '{input_file}' não contém um JSON válido.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

