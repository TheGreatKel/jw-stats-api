from flask import Flask, render_template
import connexion

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

@app.route('/')
def home():
   #localhost:5000
   return render_template('home.html')

def main():
    app.run(debug=True)

main()    
