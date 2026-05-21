from sqlalchemy import text

from app.core.database import SessionLocal


def reset_dev_data() -> None:
    db = SessionLocal()

    try:
        db.execute(text("TRUNCATE TABLE stock_movements RESTART IDENTITY CASCADE"))
        db.execute(text("TRUNCATE TABLE stock_items RESTART IDENTITY CASCADE"))
        db.execute(text("TRUNCATE TABLE products RESTART IDENTITY CASCADE"))
        db.execute(text("TRUNCATE TABLE stock_locations RESTART IDENTITY CASCADE"))

        db.commit()

        print("Development data reset successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    reset_dev_data()
