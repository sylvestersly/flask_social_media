from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Josh Doe',
        'title': '1st Post',
        'content': 'This is the first social post',
        'date_posted':'01 March, 2019'
    },

    {
        'author': 'Jane Doe',
        'title': '2nd Post',
        'content': 'This is the second social post',
        'date_posted': '02 March, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)

