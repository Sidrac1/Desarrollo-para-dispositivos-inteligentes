from sqlmodel import SQLModel, create_engine, Session

sqlite_url = "sqlite:///./Sidrac.db"
"""
El primero, sqlite_url es la cadena de conexión.
Indica al motor que usaremos el dialecto de SQLite y la ruta exacta del arhivo local (./Sidrac.db)

El segundo argumento es echo=True
si "echo" significa exo o repetición, y lo activamos en el motor de la base de datos

SQLite fue diseñado originalmente para aplicaciones de escritorio de un solo hilo (single thread)
Por seguridad tiene una restricción por defecto: solo permite que el hilo de python que creó la conexión sea
"""
engine = create_engine(sqlite_url,echo=True, connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

    def get_session():
        with Session(engine) as session:
            yield session