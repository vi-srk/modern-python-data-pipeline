# Modern Python Data Engineering Mastery 🚀

Welcome to the **Modern Python Data Engineering Mastery** repository. This project is a production-grade, 8-week progressive curriculum designed to take engineers from writing basic scripts to building scalable, memory-efficient, robust, and observable data pipelines.

Unlike traditional software or data science repos, this project builds **one single, evolving end-to-end data pipeline** from scratch—adding memory safety, modern analytical engines, data contracts, concurrency, and orchestration week by week.

---

## 📂 Repository Architecture

```text
modern-python-data-pipeline/
├── .github/workflows/          # CI/CD pipelines (GitHub Actions running Ruff & Pytest)
├── week1_streaming/            # Week 1: Memory-efficient generators & flattening
├── week2_api_ingestion/        # Week 2: Resilient API extraction & structlog
├── week3_polars_duckdb/        # Week 3: Lazy Polars transforms & DuckDB analytics
├── week4_postgres_loader/      # Week 4: Docker Postgres, bulk COPY & upserts
├── week5_data_contracts/       # Week 5: Pydantic v2 validation & Pytest suites
├── week6_concurrency/          # Week 6: Asyncio I/O & ProcessPoolExecutor CPU scaling
├── week7_pyspark/              # Week 7: Distributed PySpark & catalyst optimization
├── week8_orchestration/        # Week 8: Typer CLI & Dagster/Airflow workflows
├── .gitignore                  # Excludes .venv, .env, *.jsonl, *.parquet, *.db
├── pyproject.toml              # Unified project config & dependencies managed by uv
├── uv.lock                     # Strict lockfile for absolute reproducibility
└── README.md                   # Comprehensive master documentation for learners