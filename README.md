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

This is a brilliant request. To make this repository a world-class resource, we need a crystal-clear narrative that bridges the gap between absolute beginners and production data engineering concepts.

Here is the **End-to-End Data Lifecycle Flow** of our project. This exact narrative should live right at the top of your master `README.md` so anyone landing on your GitHub repo immediately understands how all 8 weeks connect into **one single, evolving data pipeline**.

---

# 🚀 The End-to-End Data Pipeline Flow

> **The Big Picture:** In traditional software tutorials, you build isolated "toy scripts" that don't talk to each other. In this project, you build **one single, continuous data pipeline** that grows in sophistication week by week—moving from local files to resilient APIs, high-speed columnar storage, databases, runtime data contracts, concurrency, distributed clusters, and enterprise orchestration.

---

## 🔄 The 8-Week Data Lifecycle Journey

### **Phase 1: Local Foundations & Memory Safety**

* **Week 1: Memory-Efficient Streaming (`week1_streaming/`)**
* *What happens here:* Data enters the system. Instead of loading multi-gigabyte files into RAM (which causes Out-Of-Memory/OOM crashes), we use Python generators (`yield`) to stream records line-by-line, recursively flatten nested JSON structures, and verify our memory footprint using `tracemalloc`.



### **Phase 2 & 5: External Extraction & Guardrails**

* **Week 2: Resilient API Ingestion (`week2_api_ingestion/`)**
* *What happens here:* Data streams from external web sources. Because network calls fail and APIs enforce strict rate limits (HTTP 429), we wrap our HTTP requests in an exponential backoff retry loop using `tenacity` and replace print statements with structured JSON observability (`structlog`).


* **Week 5: Data Contracts & Validation (`week5_data_contracts/`)**
* *What happens here:* Before untrusted upstream data poisons our pipeline, we enforce strict **Pydantic v2 data models**. Valid records move forward; malformed or corrupt records are safely diverted to a Dead Letter Queue (`dead_letter_queue.jsonl`), backed by a rigorous `pytest` suite.



### **Phase 3: High-Performance Storage & Analytics**

* **Week 3: Columnar Transformation & DuckDB (`week3_polars_duckdb/`)**
* *What happens here:* Row-by-row Python processing is too slow for analytics. We ingest our clean streams into **Polars** (using lazy evaluation `pl.LazyFrame` for zero-copy optimization) and write them out as **Zstd-compressed, Hive-partitioned Parquet files**. We then query them instantly using embedded **DuckDB** via pure SQL.



### **Phase 6: Relational Warehousing & Idempotency**

* **Week 4: High-Throughput Databases (`week4_postgres_loader/`)**
* *What happens here:* Data moves into a production relational database (PostgreSQL via Docker). To handle retries and job failures without creating duplicate rows, we load data using high-speed bulk `COPY` into staging tables, followed by atomic upserts (`INSERT ... ON CONFLICT DO UPDATE`).



### **Phase 4: Scaling & Concurrency**

* **Week 6: Asynchronous Concurrency (`week6_concurrency/`)**
* *What happens here:* As data volume scales, single-threaded I/O becomes a bottleneck. We refactor our API extraction layer to use `asyncio` and `httpx.AsyncClient` throttled by semaphores, while offloading heavy CPU compression workloads to a `ProcessPoolExecutor`.


* **Week 7: Distributed Processing (`week7_pyspark/`)**
* *What happens here:* When single-machine memory and CPU limits are finally exceeded, we scale out to distributed architecture using **PySpark**. We optimize query execution plans via the Catalyst Optimizer and use broadcast joins (`F.broadcast()`) to eliminate expensive network shuffles.



### **Phase 6: Production Automation**

* **Week 8: CLI & Orchestration (`week8_orchestration/`)**
* *What happens here:* Code isn't a pipeline until it runs automatically. We wrap our entire end-to-end journey into a parameterized command-line interface using **Typer**, and wire the steps into an orchestrator (Dagster or Airflow) to manage daily schedules, retries, and historical backfills.
