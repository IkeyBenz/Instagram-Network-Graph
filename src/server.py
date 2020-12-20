'''
The html page can't simply be opened as a file in a browser because it needs to pull data from data.json and browsers
don't support this unless there is a server serving the file. So here is a very simple server that just serves the
index.html and data.json files.
'''
from flask import Flask, send_file

def serve_html_and_data():
    app = Flask('Instagram-Network-Graph', static_url_path='')

    @app.route('/')
    def index():
        return send_file('index.html')
    
    @app.route('/data.json')
    def send_data():
        return send_file('data.json')

    app.run()

if __name__ == '__main__':
    serve_html_and_data()