from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        first_name = request.form.get( "first_name", "null" )
        last_name = request.form.get( "last_name", "null" )
        return jsonify(name= first_name + " " + last_name )
    else:
        return render_template("index.html")

if __name__=='__main__':
    app.run()
