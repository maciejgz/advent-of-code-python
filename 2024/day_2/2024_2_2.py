import os


def is_safe(report):
    """Check if a report is safe under normal conditions."""
    diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    increasing = all(1 <= diff <= 3 for diff in diffs)
    decreasing = all(-3 <= diff <= -1 for diff in diffs)
    return increasing or decreasing


def is_safe_with_dampener(report):
    """Check if a report is safe with the Problem Dampener applied."""
    for i in range(len(report)):
        # Create a new report by removing the i-th level
        new_report = report[:i] + report[i + 1:]
        if is_safe(new_report):
            return True
    return False


def count_safe_reports(data, with_dampener=False):
    """Count the number of safe reports."""
    safe_count = 0
    for line in data:
        report = list(map(int, line.split()))
        if is_safe(report):
            safe_count += 1
        elif with_dampener and is_safe_with_dampener(report):
            safe_count += 1
    return safe_count


# Example input
input_file = os.path.join(os.path.dirname(__file__), "input.txt")
with open(input_file, "r") as f:
        data = f.readlines()

# Part One: Count reports safe without dampener
safe_without_dampener = count_safe_reports(data, with_dampener=False)
print(f"Safe reports without dampener: {safe_without_dampener}")

# Part Two: Count reports safe with dampener
safe_with_dampener = count_safe_reports(data, with_dampener=True)
print(f"Safe reports with dampener: {safe_with_dampener}")
