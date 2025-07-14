from flask import Flask, render_template, request
app = Flask (__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/calculodescuento', methods=['GET','POST'])
def calculoDescuento():
    if request.method == 'POST':
        edad = int(request.form['edad'])
        nombre = str(request.form['nombre'])
        cantidadtarros = int(request.form['cantidadtarros'])
        if edad < 18:
            descuento = 0
            totalapagar = 9000 * cantidadtarros * (1-descuento)
        elif edad >=18 and edad <= 30:
            descuento = 0.15
            totalapagar = 9000 * cantidadtarros * (1-descuento)
        else:
            descuento = 0.25
            totalapagar = 9000 * cantidadtarros * (1-descuento)
        return render_template('calculodescuento.html', edad=edad, nombre=nombre, descuento=descuento, cantidadtarros=cantidadtarros, totalapagar=totalapagar)
    return render_template('calculodescuento.html')

@app.route('/iniciosesion',methods=['GET','POST'])
def iniciarSesion():
    mensaje=''
    if request.method == 'POST':
        usuario = str(request.form['usuario'])
        password = str(request.form['password'])
        usuariosdicc = {"juan": "admin", "pepe": "user" }
        if usuario in usuariosdicc and usuariosdicc[usuario] == password:
            if usuario == "juan":
                mensaje = 'Bienvenido administrador juan'
            else:
                mensaje = 'Bienvenido usuario '+usuario
        else:
            mensaje = 'Usuario o contraseña incorrectos.'
        return render_template('iniciosesion.html', usuario=usuario, mensaje=mensaje)
    return render_template('iniciosesion.html')

if __name__ == "__main__":
    app.run(debug=True)