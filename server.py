from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
   #localhost:5000/
   return render_template('home.html')

def main():
    app.run(debug=True)

main()    
