from flask import Flask, render_template


app = Flask(__name__)


###############################
############ MAIN #############
###############################


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/book')
def book():
    return render_template('book.html')

@app.route('/product')
def product():
    return render_template('product.html')
###############################
############ ERROR ############
###############################

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
