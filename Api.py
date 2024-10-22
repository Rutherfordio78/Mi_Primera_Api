# -*- coding: utf-8 -*-

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/lista1', methods=['GET'])

def obtener_lista1():
    datos = {
        "nombre": "Sebastian",
        "edad": 19,
        "residencia": "Seseña"}
    return jsonify(datos)

@app.route('/api/lista2', methods=['GET'])

def obtener_lista2():
    lista_datos = [
        {"nombre": "Sebastian", "edad": 19, "residencia": "Seseña"},
        {"nombre": "Tymur", "edad": 20, "residencia": "Seseña"},
        {"nombre": "Javi", "edad": 19, "residencia": "Seseña"}
        ]
    return jsonify(lista_datos)

if __name__ == "__name__":
    app.run(debug=True)


