# Crie o arquivo README.md
echo "# Gerando JSON Faker" > README.md

# Adicione o arquivo ao staging
git add README.md

# Faça o primeiro commit
git commit -m "Primeiro commit"

# Renomeie a branch para 'main' se necessário
git branch -M main

# Envie a branch 'main' para o repositório remoto
git push -u origin main
