from flask import Flask
app = Flask(__name__)

@app.route('/baseball')
def baseball():
    return '여기는 야구페이지'

@app.route('/football')
def football():
    return '''
    <html>
    <body>

    <h2>여기는 축구페이지</h2>
    <img src="https://imgnews.pstatic.net/image/436/2021/05/17/0000044110_001_20210517114805981.jpg?type=w647">

    </body>
    </html>
    '''

@app.route('/volleyball')
def volleyball():
    return '여기는 배구페이지'

if __name__ == '__main__':
    app.run()