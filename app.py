from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Flask!"


if __name__ == "__main__":
    app.run(
        debug=True
    )  # ! IMPORTANT: Remove "debug=True" before deploying to production

    """
    ## Hi
    ### Hello
    NOTE: Hte
    IMPORTANT:
    * Hello
    
    
    """
    """
    * ! Hello
    """
    # * ! Hello
    # ! Hey there!
    # ? What's up?
    # // DONE
    # % Hey
    # $ Hello
    # @ Hello
    # & Hi
    # - There is none
    # # YO YO
    """
    @ hello
    
    """
