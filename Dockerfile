# 1. Base Image
FROM python:3.12-slim

# 2. Install uv for fast dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 3. Set working directory
WORKDIR /app

# 4. Copy configuration files
COPY pyproject.toml uv.lock ./

# 5. Install dependencies using uv
RUN uv sync --frozen --no-cache

# 6. Copy all project files (main.py and the app/ folder)
COPY . .

# 7. Start the app by running main.py
# We use the python inside the .venv created by uv
CMD ["/app/.venv/bin/python", "main.py"]