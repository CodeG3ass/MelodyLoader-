# MelodyLoader-

## Backend (FastAPI)

Локальный запуск из корня проекта (Python 3.12):

```powershell
cd src/backend
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Запуск backend через Docker из корня проекта:

```sh
docker compose up --build backend
```

- API: http://localhost:8000/
- Проверка работы приложения: http://localhost:8000/health
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

Точка входа — `src/backend/app/main.py`, маршруты — `src/backend/app/api/router.py`.
Маршрут `/health` проверяет только работу приложения, без подключения к внешним сервисам.
