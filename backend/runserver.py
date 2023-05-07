from services import create_app

app = create_app()

# SQLALCHEMY_DATABASE_URI='sqlite:///db.db'
# SQLALCHEMY_DATABASE_URI=postgresql://alihan0810:lexa_ne_lox@osi-database-1:5432/osi_help

if __name__ == "__main__":
    app.run(host="0.0.0.0")
