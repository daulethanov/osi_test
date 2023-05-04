from services import create_app

app = create_app()

# SQLALCHEMY_DATABASE_URI='postgresql://postgres:1234@database:5432/dbname'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
