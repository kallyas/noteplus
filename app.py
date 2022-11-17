import os
from notesapp import create_app, db


app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Tables created")
    PORT = int(os.environ.get('PORT', 8000))
    app.run('0.0.0.0', PORT)
