from flask import Flask, render_template, request


app = Flask(__name__)
app.secret_key = 'dev key'  # TODO: move to settings

from forms import SearchForm
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()

    if request.method == 'POST':
        return 'Form posted'

    elif request.method == 'GET':
        return render_template('search.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
