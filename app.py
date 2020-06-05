from flask import Flask , render_template , redirect , url_for

app = Flask(__name__)

@app.route("/" , methods=['POST' , 'GET'])
def home():
    return render_template("index.html")


@app.route("/gallery" , methods=['POST' , 'GET'])
def gallery():
    #return redirect(url_for('gallery',_anchor='gallery.html'))
    return render_template("gallery.html")

@app.route("/events" , methods=['POST' , 'GET'])
def events():
    #return redirect(url_for('gallery',_anchor='gallery.html'))
    return render_template("events.html")

@app.route("/team" , methods=['POST' , 'GET'])
def team():
    return render_template("team.html")

app.run(debug=True)