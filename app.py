from chalice import Chalice

app = Chalice(app_name='troubleshooting-chalice')


@app.route('/')
def index():
    return {'hello': 'world'}

