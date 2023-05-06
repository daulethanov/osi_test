from services import create_app

app = create_app()

# SQLALCHEMY_DATABASE_URI='sqlite:///db.db'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
