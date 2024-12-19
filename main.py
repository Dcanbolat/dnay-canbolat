import os

from flask import Flask, send_file, render_template
from random import randint, choice


app = Flask(__name__)

@app.route("/")
def index():
    return send_file('src/index.html')

@app.route("/yemek")
def yemek():
    yemekler = "Döner", "Brokoli", "Karnabahar", "Fasulye"
    gununyemegi = choice(yemekler)
    return render_template("yemek.html", data=gununyemegi)



@app.route("/loto")
def loto_route():
    
    i = 0
    secilenler = [0,0,0,0,0,0,0,0]
    goster = []
    for rastgele in secilenler:
        while i < len(secilenler):
            secilen = randint(1, 100)
            if secilen not in secilenler:
                secilenler[i] = secilen
                i+=1
        goster.append(sorted(secilenler))
        i=0

    return render_template("loto.html", data=goster)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()