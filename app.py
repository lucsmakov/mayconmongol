from flask import Flask, render_template
from routes.user_route import users_bp
#
app = Flask(__name__)
app.register_blueprint(users_bp)
@app.route('/')
def webHome():
    return render_template('u.html')

if __name__ == '__main__':
    app.run(debug=True)