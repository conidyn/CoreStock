from sqlalchemy import text

from alembic import command
from alembic.config import Config

from app.core.database import engine


def pytest_sessionstart(session):
    with engine.connect() as connection:
        connection.execute(text("DROP SCHEMA public CASCADE"))
        connection.execute(text("CREATE SCHEMA public"))
        connection.commit()

    alembic_config = Config("alembic.ini")
    command.upgrade(alembic_config, "head")
