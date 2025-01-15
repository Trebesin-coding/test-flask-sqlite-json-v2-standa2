# Z následujících si vyber kód a sestav funkční flask aplikaci (není třeba použít vše, vyber si pouze ty části kódu, které potřebuješ)
# Kód je funkční, pouze místo dotazníků je potřeba doplnit podle potřeby


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("vitej.html")

@app.route("/form")
def form():
    py = request.args.get("recenze")
    if py == "nic":
        py = "uživatel byl příliš líný na napsání recenze"
    return render_template("form.html", jinja = py)





# request.form.get("???")
# print("???")
# cursor.execute("???")


if __name__ == "__main__":
    app.run(debug=True)
# 
