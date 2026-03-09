# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
# Passo 2: Fazer login
# Passo 3: Pegar/Importar a base de dados 
# Passso 4: Cadastrar um produto
# Passo 5: Repetir o passo 4 até cadastrar todos os produtos
# Link do site: https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time # biblioteca que controla o tempo
# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever um texto
# pyautogui.press - apertar 1 tecla
# pyautogui.hotkey - combinação de teclas (Ctrl C)
# pyautogui.scroll - rolar a tela para cima ou para baixo

pyautogui.PAUSE = 0.5 # PAUSE é uma configuração, de tempo, em que a cada comando pyautogui vai dá uma pausa de 0.5 segundos.

# Passo 1 - Entrar no sistema
# Abrir o navegador
pyautogui.press("win") # nome da tecla por isso que fica entre aspas.
# Digitar chrome
pyautogui.write("chrome")
#Apertar enter para abrir navegador
pyautogui.press("enter")

# Entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3) # espera 3 segundos apenas no local específico.

# Passo 2 - Fazer login
pyautogui.click(x=576, y=372)
pyautogui.hotkey("ctrl", "a")
# Digitar o emai
pyautogui.write("pedrinvinicin777@gmail.com")
# Passar para o campo de senha
pyautogui.press("tab")
# Digitar senha
pyautogui.write("1234")
# Clicar no botão de logar
pyautogui.click(x=671, y=544)

time.sleep(3)

# Passo 3 - Importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Passo 4 - Cadastrar o produto 
for linha in tabela.index: # .index é uma lista com todas as linhas da tabela 
    pyautogui.click(x=525, y=258)
    # tabela.loc[linha, coluna]
    # tabela.loc[1, "codigo"]

    # codigo
    codigo = str(tabela.loc[linha, "codigo"]) # string = texto 
    pyautogui.write(codigo)

    # marca
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)

    # tipo 
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)

    # categoria
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    # preco_unitario
    pyautogui.press("tab")
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)

    # custo
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    # obs
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    

    # clicar no botao enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

# Passo 5 - Repetir para todos os produtos - para todas as linhas da tabela
