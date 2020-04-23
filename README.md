# Flask-SQLAlchemy Database Connection

This is a working example of a backend app monitoring log files from a running icecast server on Fedora, writing these changes to a sqlite database.

It demonstates how to set the flask app using application factory and how to deal with application context and circular references. It also shows how to use a watchdog notifier (a handler constantly monitoring a change in a particular file) and how to run in within application context.
