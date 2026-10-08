def should_retry(job, max_retries=2):
    """
    Decide whether a failed CI job should be retried.

    Args:
        job (dict):
            {
                "status": str,
                "attempts": int,
                "failure_type": str,
            }

        max_retries (int): Maximum number of attempts allowed.

    Returns:
        bool: True if the job should be retried.
    """

    if job["status"] == "passed":
        return False

    if job["attempts"] >= max_retries:
        return False

    if job["failure_type"] in ("timeout", "network"):
        return True

    if job["failure_type"] == "assertion":
        return False

    return False
