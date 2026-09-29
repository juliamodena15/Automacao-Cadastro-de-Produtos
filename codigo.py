import pyautogui
import time

link = "http://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 0.5

#Caminho até a pagina
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=843, y=611)
pyautogui.click(x=440, y=71)
pyautogui.write(link)
pyautogui.press("enter")

#Login
time.sleep(3)

pyautogui.click(x=692, y=464)
pyautogui.write("julia@gmail.com")
pyautogui.press("tab")
pyautogui.write("julia1234")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("enter")

time.sleep(1)
pyautogui.press("enter")
pyautogui.click(x=1659, y=462)
pyautogui.press("enter")

#Cadastro de Produtos
import pandas

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=663, y=330)
    #Código
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #Marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    #Tipo de Produto
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #Categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #Preco
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    #Custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    #Obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab") #tab para o enviar

    pyautogui.press("enter")
    pyautogui.scroll(5000) #ir para o inicio

