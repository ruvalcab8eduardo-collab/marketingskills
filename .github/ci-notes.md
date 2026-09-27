CI notes

Local reproduction commands:

# Crear y activar virtualenv
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Crear sqlite test DB si se usa test.db
touch ./test.db

# Ejecutar linters
ruff . || true
black --check . || true
mypy . || true

# Ejecutar pruebas
pytest -q --maxfail=1
