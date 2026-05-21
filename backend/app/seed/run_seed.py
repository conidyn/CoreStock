from app.core.database import SessionLocal
from app.seed.demo_data import seed_demo_data


def run() -> None:
    db = SessionLocal()

    try:
        seed_demo_data(db)

    finally:
        db.close()


if __name__ == "__main__":
    run()
