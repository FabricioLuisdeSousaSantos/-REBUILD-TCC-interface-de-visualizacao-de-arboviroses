#REBUILD - SISTEMA DE VISUALI. DE ARBOVIROSES 
# ESTRUTURA
1. sistema_de_avaliacao.py - Arquivo Main do sistema
2. baixar_dados.py - Arquivo que baixa os dados
3. calculo_incidencia.py - Faz o calculo de incidencia por 100k hab.
4. previsao.py - Faz a previsão 
5. atualizar_modelo.py - Faz a atualização do modelo com os dados do InfoDengue

# INSTRUÇÕES DE USO
## Instalação
1. Após baixar o repositório extraia os 03 arquivos .pkl de "modelos.7z" e os coloque na pasta ./modelos. Eles são os modelos padrão desatualizados.

## Criação de venv e rodar sistema
1. Criar venv com Python 3.12 com o UV: "uv venv --python 3.12 .venv"
2. Ative o venv em: "cd ./.venv/bin/" e depois" . activate.fish"
3. Volte para a pasta root: "cd ../.."
4. Instale as dependências no venv: "uv pip install -r requirements.txt"
5. Rode o sistema web com: "streamlit run sistema_de_avaliacao.py"

## Uso
1. Na tela selecione a arvovirose
2. Selecione a quatidade de semanas para prever
3. Clique em "Fazer previsão"
