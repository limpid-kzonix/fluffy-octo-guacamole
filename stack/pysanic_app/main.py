from app.server import app

if __name__ == "__main__":
    """Run application server"""
    app.run(host='0.0.0.0', port=1337, workers=4, debug=True, access_log=True)
