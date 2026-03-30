import pyautogui
import pandas
import time
tabela = pandas.read_csv('produtos.csv')
pyautogui.PAUSE = 1.5

link = ('https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbWtCNTJDclU5UmxlYTBaRjlMVGVibmNiUTFlQXxBQ3Jtc0tuVEtZdWFFaFA5Vl9pZnpPRmNkREJsZW5acjhqZlk3bTBpV1hwZEp1ZEdsLWhibmFrMTdnWWp2Qm41S2NJMmJhZGVvWkFOTFNZRVloblR4MTIwSHBkbDFNVWp3Nlo1RlBKNXIzZHpaaHFLZDZUN0c0UQ&q=https%3A%2F%2Fdlp.hashtagtreinamentos.com%2Fpython%2Fintensivao%2Flogin&v=0GDt-6H9NWM')
pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(x=628, y=470)
pyautogui.write('fulanodetal@gmail.com')    
pyautogui.press('tab')
pyautogui.write('senhadebigode')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(4)
pyautogui.click(x=665, y=316)

for linha in tabela.index:
    #codigo
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)    
    pyautogui.press('tab')
    #marca
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)    
    pyautogui.press('tab')
    #tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)    
    pyautogui.press('tab')
    #categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)    
    pyautogui.press('tab')
    #preco
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)    
    pyautogui.press('tab')
    #custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)    
    pyautogui.press('tab')  
    #obs
obs = str(tabela.loc[linha, 'obs'])
if obs != 'nan':
        pyautogui.write(obs)    
pyautogui.press('tab')

pyautogui.press('enter')

#voltar para o começo
pyautogui.scroll(3000)


