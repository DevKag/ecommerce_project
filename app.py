""" Main appilication file fro creating and executing app Instances"""
from source import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
