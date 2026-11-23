import json  # Parses JSON strings into Python dictionaries and serializes Python objects back to JSON text
import random  # Generates pseudo-random numbers and choices to simulate realistic mock event data
import tracemalloc  # Tracks Python memory allocations in real time to measure peak RAM usage during streaming
from typing import Any, Dict, Generator  # Provides static type hints for flexible values, dictionaries, and generator functions
import uuid  # Generates unique UUIDs so every simulated event gets a distinct event_id


def generate_mock_stream(file_path: str, num_records: int = 300_000):
    """Generates a massive, deeply nested JSONL file to test streaming memory limits.

    Designed to simulate multi-gigabyte production data streams without OOM crashes.
    """
    
    print(f"Generating {num_records} mock nested records to {file_path}...")
    with open(file_path, "w", encoding="utf-8") as f:
        for i in range(num_records):
            record = {
                "event_id": str(uuid.uuid4()),
                "timestamp": f"2026-11-{random.randint(1,30):02d}T10:00:00Z",
                "user": {
                    "id": random.randint(1000, 9999),
                    "profile": {
                        "country": random.choice(["US", "CA", "GB", "DE", "IN"]),
                        "tier": random.choice(["free", "pro", "enterprise"]),
                    },
                },
                "metrics": {
                    "cpu_load": round(random.uniform(0.1, 0.99), 4),
                    "memory_mb": random.randint(512, 16384),
                },
            }
            f.write(json.dumps(record) + "\n")
            if i > 0 and i % 100_000 == 0:
                print(f"Written {i} records...")
    print("Mock generation complete.")


def flatten_dict(d: Dict[str, Any], parent_key: str = "", sep: str = "_") -> Dict[str, Any]:
    """Recursively flattens nested dictionaries for tabular transformations."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def stream_jsonl_file(file_path: str) -> Generator[Dict[str, Any], None, None]:
    """Generator function that yields one line at a time from disk.

    Crucial pattern for preventing Out-Of-Memory (OOM) errors on large datasets.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                raw_record = json.loads(line)
                flattened = flatten_dict(raw_record)
                
                # Normalize and clean fields safely using .get() defaults
                cleaned_record = {
                    "event_id": flattened.get("event_id", "UNKNOWN"),
                    "timestamp": flattened.get("timestamp"),
                    "country": flattened.get("user_profile_country", "UNKNOWN"),
                    "tier": flattened.get("user_profile_tier", "unknown"),
                    "cpu_load": flattened.get("metrics_cpu_load", 0.0),
                    "memory_mb": flattened.get("metrics_memory_mb", 0),
                }
                yield cleaned_record
            except json.JSONDecodeError:
                continue


if __name__ == "__main__":
    input_file = "week1_streaming/large_events.jsonl"
    output_file = "week1_streaming/clean_events.jsonl"

    # 1. Generate the heavy mock dataset
    generate_mock_stream(input_file, num_records=300_000)

    # 2. Run the streaming pipeline with tracemalloc memory tracking
    print("\nStarting memory-efficient streaming pipeline...")
    tracemalloc.start()

    total_processed = 0
    with open(output_file, "w", encoding="utf-8") as out_f:
        for record in stream_jsonl_file(input_file):
            out_f.write(json.dumps(record) + "\n")
            total_processed += 1

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Successfully streamed and processed {total_processed} records.")
    print(f"Peak Memory Usage: {peak / 1024 / 1024:.2f} MB")