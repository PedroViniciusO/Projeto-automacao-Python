# Automação de Cadastro de Produtos 🤖

## Descrição
Este projeto é um script de automação desenvolvido em Python para otimizar tarefas repetitivas de entrada de dados (Data Entry). O código simula interações com o computador (mouse e teclado) para acessar um sistema web, realizar o login e cadastrar sequencialmente uma lista de produtos extraída de uma base de dados.

## Funcionalidades
* **Automação de Navegação:** Abertura automática do navegador e acesso ao sistema da empresa.
* **Login Automatizado:** Inserção automática de e-mail e senha.
* **Leitura e Processamento de Dados:** Importação das informações dos produtos a partir de um arquivo .csv.
* **Cadastro em Massa:** Preenchimento sequencial dos formulários de cadastro com os dados extraídos, incluindo tratamento para campos vazios (como observações).

## Tecnologias e Bibliotecas Utilizadas
* **Python:** Linguagem de programação.
* **PyAutoGUI:** Para o controle programado do mouse e teclado.
* **Pandas:** Para a leitura, integração e manipulação da base de dados.
* **Time:** Para o gerenciamento de pausas e sincronização de tempo de carregamento das páginas.

## Estrutura do Projeto
* `main.py` (ou o nome que você deu ao arquivo principal): Contém o código com o passo a passo da automação.
* `aux.py`: Script auxiliar utilizado para mapear as coordenadas (X, Y) do monitor, facilitando a configuração exata dos cliques do mouse.
* `produtos.csv`: Base de dados estruturada contendo as informações dos produtos que serão cadastrados.