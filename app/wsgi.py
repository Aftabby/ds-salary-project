from app import app  # Import the Flask application instance

if __name__ == "__main__":
    app.run(debug=True)  # IMPORTANT: Remove "debug=True" before deploying to production
