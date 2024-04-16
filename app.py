from flask import Flask, redirect, url_for, request, abort

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      data = request.get_json()
      name = data['name']
      return redirect(url_for('success',name = name))
   else:
      user = request.args.get('name')
      return redirect(url_for('success',name = user))

@app.route('/error')
def error():
    abort(500)
    



if __name__ == '__main__':
    app.run(debug=True)