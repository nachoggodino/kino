# Makefile

# === BACKEND ===
run-back:
	uvicorn app.main:app --reload --reload-dir app --port=8000

# === FRONTEND ===
run-front:
	PYTHONPATH=. streamlit run frontend/main.py

# === COMBINED ===
kino:
	@echo "🚀 Launching Kino: Backend + Frontend"
	@make run-back & make run-front

# === TESTS ===
test:
	PYTHONPATH=./app pytest -v --tb=short

# === STOP BACKEND ===
stop-back:
	@pkill -f "uvicorn"

# === STOP FRONTEND ===
stop-front:
	@pkill -f "streamlit"

# === STOP ALL ===
stop-all:
	@make stop-back
	@make stop-front
	@echo "🛑 Kino backend and frontend stopped."

# === RESTART ALL ===
restart:
	@make stop-all
	@sleep 1
	@make run-back
	@make run-front
	@echo "🔄 Kino restarted."

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
