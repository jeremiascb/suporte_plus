from app import app
from utils.db import db

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host='192.168.1.117', port=5000, debug=True)