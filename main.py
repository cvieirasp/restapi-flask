from application import create_app

app = create_app('application.config.Config')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
