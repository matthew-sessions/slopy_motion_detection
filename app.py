from flask import Flask, render_template
import os


app = Flask(__name__, static_folder="static")

@app.route("/")
def vids():
    files = os.listdir("static")
    names = ""
    for file in files:
        names += file + "\n"
    return names

@app.route("/delete")
def delete():
    files = os.listdir("static")
    for file in files:
        os.remove(f"static/{file}")
    return "done"


@app.route('/<file>')
def index(file):
    return render_template('index.html', 
        movie_name=file + ".mp4",
        movie_ext='mp4')

if __name__ == '__main__':
    app.run()
