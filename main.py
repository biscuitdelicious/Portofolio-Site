from flask import Flask, render_template

root = Flask(__name__)


@root.route('/')
def main():
    return render_template('index.html')


@root.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@root.route('/about')
def about_me():
    return render_template('about_me.html')


if __name__ == '__main__':
    root.run(debug=True)
