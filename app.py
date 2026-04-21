from flask import Flask, redirect, request, url_for,render_template
import sqlite3

app = Flask(__name__)

def init_database():
    conn = sqlite3.connect("inventario.db")
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS productos(
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()
init_database()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/registronuevo",methods=['POST'])
def registronuevo():
    nombre = request.form['nombre']
    categoria = request.form['categoria']
    precio = request.form['precio']
    stock = request.form['stock']

    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO productos(nombre,categoria,precio,stock)
        VALUES(?,?,?,?)
        """,(nombre, categoria, precio, stock)
    )
    conn.commit()
    conn.close()
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)