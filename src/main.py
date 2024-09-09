from . import create_app

app = create_app()

@app.route('/', methods=["GET"])
def root():
    return {'success': ['Hello World']}, 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
