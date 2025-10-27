FROM agrigorev/zoomcamp-model:2025

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PATH="/code/.venv/bin:$PATH"

COPY "pyproject.toml" ".python-version" "uv.lock" ./

RUN uv sync --locked

COPY "predict.py" ./

EXPOSE 8000

ENTRYPOINT ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]
