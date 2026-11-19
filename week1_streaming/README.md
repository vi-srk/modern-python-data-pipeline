# Week 1: Memory-Efficient Streaming & JSON Flattening

## 1. Goal & Real-World Problem
In real-world data engineering, pipelines often read large JSON Lines (`.jsonl`) files or event streams containing deeply nested objects. A common beginner mistake is loading an entire file into RAM at once (for example, reading all lines into a list). On large datasets, that spikes memory usage and can crash a process with an **Out-Of-Memory (OOM)** error.

In this module, we build a **streaming ingestion and normalization pipeline** that:
- Generates a self-contained local dataset (`large_events.jsonl`) so anyone can run the script without depending on external file links or large downloads.
- Streams records one at a time using a Python generator (`yield`) instead of holding all records in memory.
- Recursively flattens nested JSON dictionaries into flat fields and safely extracts values with defaults.
- Measures peak memory consumption programmatically using `tracemalloc`.

---

## 2. How the Code Works (`week1_streaming/main.py`)

### A. Self-Contained Mock Data Generator (`generate_mock_stream`)
- **Why it exists:** Public datasets can have broken URLs, slow downloads, or large initial clone sizes. Generating synthetic data locally makes the repository reproducible anywhere with a single command.
- **What it does:** Writes `300,000` nested JSON event records (each with `event_id`, `timestamp`, nested `user.profile`, and nested `metrics`) line by line to `week1_streaming/large_events.jsonl`, printing progress every `100,000` records.

### B. Recursive Dictionary Flattening (`flatten_dict`)
- **Why it exists:** Nested JSON objects (like `{"user": {"profile": {"country": "IN"}}}`) are awkward to normalize or map into flat tabular schemas.
- **What it does:** Walks through nested `dict` values recursively and joins keys with `_` (producing keys such as `user_profile_country` and `metrics_cpu_load`), while leaving non-dictionary values intact.

### C. Lazy Streaming Generator (`stream_jsonl_file`)
- **Why it exists:** Returning a list of hundreds of thousands of parsed/flattened dictionaries keeps all of them in RAM at once. Using `yield` turns the function into a **generator** that produces one cleaned record at a time on demand.
- **What it does:**
  1. Opens `large_events.jsonl` and iterates line by line.
  2. Skips blank lines and safely ignores malformed JSON lines (`JSONDecodeError`) instead of crashing the entire run.
  3. Flattens each record and builds a normalized dictionary using `.get(...)` with fallback defaults so missing optional fields do not raise `KeyError`.
  4. `yield`s each `cleaned_record` to the caller.

### D. Memory Verification (`tracemalloc`)
- **Why it exists:** Claims about "low memory usage" should be measured, not guessed.
- **What it does:** Starts `tracemalloc` around the streaming loop that reads from `stream_jsonl_file` and writes normalized rows to `week1_streaming/clean_events.jsonl`, then reports the peak traced memory in megabytes.

---

## 3. How to Run It

From the root of the repository (`modern-python-data-pipeline`), run:

```powershell
uv run week1_streaming/main.py