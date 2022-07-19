import logging

#import azure.functions as func

from flask import Flask


app = Flask(__name__)
@app.route("/hello/<name>", methods=['GET'])
def hello(name: str):
    return f"hello {name}"

@app.route("/module")
def module():
    return f"Module page accessed"


@app.route("/")
def index():
    return (
        "Try /hello/Chris for parameterized Flask route.\n"
        "Try /module for module import guidance"
    )

if __name__ == "__main__":
    app.run()