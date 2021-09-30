#10> Create a tracker for information about Covid-19.

from typing import Text
import requests
import tkinter as tk 
import bs4


def get_data(url):
    data = requests.get(url)
    return data

def Covid_data():
    url= "https://www.worldometers.info/coronavirus/"
    data1 = get_data(url)
    bs = bs4.BeautifulSoup(data1.text, 'html.parser')
    in_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")

    allData=""

    for block in in_div:
        text = block.find("h1", class_=None).get_text()

        count= block.find("span", class_=None).get_text()
        
        allData = allData + text + " " + count + "\n"

    return allData


def countries_data():
    name = textField.get()
    url = 'https://www.worldometers.info/coronavirus/#countries/'+name
    data1 = get_data(url)
    bs = bs4.BeautifulSoup(data1.text, "html.parser")
    in_div = bs.find('div', class_= "content-inner").findAll("div", id= "maincounter-wrap")
    
    allData= ""
    for block in in_div:
        text = block.find("h1", class_= None).get_text()
        count = block.find("span", class_= None).get_text()
        allData = allData + text + " " + count + "\n"
    mainLable["text"] = allData




def  reset():
    new_data = Covid_data()
    mainLable['text'] = new_data


Covid_data()

root = tk.Tk()
root.geometry("700x540")
root.title("Covid Track")
font = ("Times new roman ", 25, "bold")

banner = tk.PhotoImage(file="covid-19.png")
bannerLable = tk.Label(root, image=banner)
bannerLable.pack()
textField = tk.Entry(root, width= 70)
textField.pack()
mainLable= tk.Label(root, text= Covid_data(), font=font)
mainLable.pack()

gn = tk.Button(root, text= "Enter", font=font, relief="solid", command= countries_data)
gn.pack()

rn = tk.Button(root, text= "Reset", font=font, relief="solid", command=reset)
rn.pack()

root.mainloop()