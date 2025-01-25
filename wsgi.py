from app import app  # Import your Flask app instance
import os

if __name__ == "__main__":
    # Enable template auto-reloading for development
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    # Get the PORT from environment variables, fallback to 5000 for local use
    port = int(os.environ.get("PORT", 5000))

    # Run the app with the proper host and port
    app.run(host="0.0.0.0", port=port)
