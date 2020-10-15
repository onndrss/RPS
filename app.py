from flask import Flask, render_template
from random import choice

app = Flask(__name__)
app.debug = True
def nahodny():
    return choice (["Kámen","Nůžky","Papír"])

@app.route('/')
def vyber():
    return render_template("vyber.html")

def vyhra(hrac, pocitac):
    if hrac == pocitac:
        return "Remiza"
    if hrac == "Kámen" and pocitac == "Nůžky":
        return "Vyhral jsi !"
    if hrac == "Nůžky" and pocitac == "Papír":
        return "Vyhral jsi !"
    if hrac == "Papír" and pocitac == "Kámen":
        return "Vyhral jsi !"
    return "Prohral jsi!"

@app.route('/kamen')
def kamen():
    hrac = "Kámen"
    pocitac = nahodny()
    vyhra2 = vyhra(hrac,pocitac)
    return render_template("hra.html",pocitac=pocitac,hrac=hrac,vyhra=vyhra2)

@app.route('/papir')
def papir():
    hrac = "Papír"
    pocitac = nahodny()
    vyhra2 = vyhra(hrac,pocitac)

    return render_template("hra.html",pocitac=pocitac,hrac=hrac,vyhra=vyhra2)

@app.route('/nuzky')
def nuzky():
    hrac = "Nůžky"
    pocitac = nahodny()
    vyhra2 = vyhra(hrac,pocitac)

    return render_template("hra.html",pocitac=pocitac,hrac=hrac,vyhra=vyhra2) 




if __name__ == '__main__':
    app.run()
