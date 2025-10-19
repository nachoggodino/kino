# Makefile

# === BACKEND ===
run-back:
	PYTHONPATH=./app uvicorn app.main:app --reload --port 8000

# === FRONTEND ===
run-front:
	cd frontend && streamlit run main.py

# === TESTS ===
test:
	PYTHONPATH=./app pytest -v --tb=short

# === CLEAN CACHE ===
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +

# === HELP ===
help:
	@echo "Available commands:"
	@echo "  make run-back      → Launch FastAPI backend"
	@echo "  make run-front     → Launch Streamlit frontend"
	@echo "  make test          → Run all tests"
	@echo "  make clean         → Remove Python cache"
