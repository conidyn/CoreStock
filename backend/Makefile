TEST_DATABASE_URL=postgresql+psycopg://corestock_user:corestock_password@localhost:5432/corestock_test

test:
	DATABASE_URL=$(TEST_DATABASE_URL) pytest

run:
	uvicorn app.main:app --reload