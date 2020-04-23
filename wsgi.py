   
from application.notifier import app, notify 


def main():
    notify()
    app.run(host='localhost')


if __name__== "__main__":
    main()
