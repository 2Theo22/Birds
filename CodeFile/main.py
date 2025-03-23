#import app package from innit to run app

from website import create_app

app = create_app()

#only if we run this file this line will be executed
if __name__ == '__main__':
    app.run(debug = True)
