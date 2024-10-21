import pyautogui
import time
import pandas

pyautogui.PAUSE = 2

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=428, y=387)
pyautogui.write("antonio.irineu@empresa.com")
pyautogui.press("tab")
pyautogui.write("12345678")
pyautogui.click(x=671, y=550)

time.sleep(5)

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:

    pyautogui.click(x=437, y=279)
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)



