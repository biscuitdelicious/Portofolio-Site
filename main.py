from flask import Flask, render_template

root = Flask(__name__)


@root.route('/')
def main():
    return render_template('index.html')


@root.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


if __name__ == '__main__':
    root.run(debug=True)
