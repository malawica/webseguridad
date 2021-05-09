from flask import Flask, jsonify, request, render_template


app = Flask(__name__)



@app.route('/html_test')
def hello_html():
    # html file은 templates 폴더에 위치해야 함
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
