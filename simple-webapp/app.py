from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Get client request header
    client_request_header = request.headers

    # Get server information
    server_info = {
        'Server': request.host,
        'Host': request.host_url,
        'Remote Addr': request.remote_addr
    }

    # Set response headers
    response_headers = {
        'Content-Type': 'text/html',
        'Custom-Header': 'Custom Value'
    }

    return render_template('index.html', client_request_header=client_request_header, server_info=server_info, response_headers=response_headers)

# flask default port=5000
if __name__ == '__main__':
    app.run(host="0.0.0.0")
