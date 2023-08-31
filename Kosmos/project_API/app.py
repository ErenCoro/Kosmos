from flask import Flask, request, jsonify
import ml_model.model as entidades



app = Flask(__name__)

#debe ser mismo nombre el de la ruta que el de la funcion 
@app.route('/procesar_oraciones', methods=['POST'])

def procesar_oraciones():
    data = request.get_json()

    #mandar error si no se recibe un JSON donde las oraciones vengan nombradas con 'oraciones'
    #o se encuentre vacio el JSON 
    if 'oraciones' not in data:
        return jsonify({'error': 'Lista de oraciones no proporcionadas'}), 400


    #continuar con el proceso si los datos recibidos son los correctos 
    oraciones = data['oraciones']
    entidades_oraciones = entidades.reconocimiento_entidades(oraciones)
    
    return jsonify({'resultado': entidades_oraciones})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
