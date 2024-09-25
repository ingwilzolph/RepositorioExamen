from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/calculoCompras', methods=['GET', 'POST'])
def calculoCompras():
  if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        resultado = tarros * 9000
        if edad >= 18 and edad <= 30 :
           descuento = resultado * 0.15
        elif edad > 30 :
           descuento = resultado * 0.25
        else :
           descuento = 0
        return render_template('calculoCompras.html', resultado=resultado, descuento=descuento, nombre=nombre, edad=edad, tarros=tarros)
  else :
      return render_template('calculoCompras.html')


@app.route('/inicioSesion', methods=['GET', 'POST'])
def inicioSesion():
      if request.method == 'POST':
          nombre = request.form['nombre']
          palabra_secreta = request.form['palabra_secreta']
          mensaje = ''
          if nombre == 'juan' and palabra_secreta == 'admin':
              mensaje = 'Bienvenido Administrador '+nombre
          elif nombre == 'pepe' and palabra_secreta == 'user':
              mensaje = 'Bienvenido Usuario '+nombre
          else:
              mensaje = 'Usuario o contraseña incorrectos'
          return render_template('inicioSesion.html', mensaje=mensaje, nombre=nombre, palabra_secreta=palabra_secreta)
      else:
        return render_template('inicioSesion.html')

if __name__ == '__main__':
    app.run(debug=True)