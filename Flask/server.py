
from flask import Flask, render_template
import datetime, time

tiempo= int(time.mktime(datetime.datetime.now().timetuple()))


import datetime

app = Flask('testapp')
#images = Images(app)


variables= [20,15,1520188605,1520188272,1520188622,1520188315,1520188831,1520188643,50,35]





@app.route('/')
def estacion():
    return render_template('main.html')
#return render_template('inicio.html', variable='12345')


@app.route('/linea3')
def lineas():
    return render_template('heatmap.html')
#return render_template('inicio.html', variable='12345')

@app.route('/info')
def info():
    return render_template('info.html')
#return render_template('inicio.html', variable='12345')

@app.route('/estaciones')
def estaciones():
    return render_template('stations.html',variable=variables)
#return render_template('inicio.html', variable='12345')


if __name__ == '__main__':
    app.run()