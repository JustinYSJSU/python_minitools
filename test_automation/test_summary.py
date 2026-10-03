def summarize_results(results):
    """Summarize a collection of test results.

    Each result should contain:
        name: str
        status: "passed", "failed", or "skipped"
        duration: float

    Returns a dictionary containing counts and total duration.
    """
    summary = {
        "passed": 0,
        "failed": 0,
        "skipped": 0,
        "total_duration": 0.0,
    }

    for result in results:
        status = result["status"]

        if status not in ("passed", "failed", "skipped"):
            raise ValueError(f"Unknown status: {status}")

        summary[status] += 1
        summary["total_duration"] += result["duration"]

    return summary