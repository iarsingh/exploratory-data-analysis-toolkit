class InputError(ValueError):
    pass


def analyze(rows):
    if not isinstance(rows, list) or not rows or not all(isinstance(r, dict) for r in rows):
        raise InputError("rows must be a non-empty list of objects")
    values = []
    groups = {}
    skipped = 0
    for row in rows:
        raw = row.get("value")
        try:
            number = float(raw)
        except (TypeError, ValueError):
            skipped += 1
            continue
        values.append(number)
        key = str(row.get("cohort", "unknown"))
        groups.setdefault(key, []).append(number)
    if not values:
        raise InputError("no numeric value values")
    values.sort()
    mid = len(values) // 2
    median = values[mid] if len(values) % 2 else (values[mid - 1] + values[mid]) / 2
    by_group = {name: round(sum(nums) / len(nums), 4) for name, nums in groups.items()}
    return {
        "rows": len(rows),
        "skipped": skipped,
        "mean": round(sum(values) / len(values), 4),
        "median": median,
        "min": values[0],
        "max": values[-1],
        "by_cohort": by_group,
    }
