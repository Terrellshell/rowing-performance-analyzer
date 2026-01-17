import csv

def read_data(filename):
    rows = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows

def calculate_stats(rows):
    distances = [int(r["distance"]) for r in rows]
    paces = [r["pace"] for r in rows]

    total_distance = sum(distances)
    fastest = min(paces)
    slowest = max(paces)

    return total_distance, fastest, slowest

def main():
    data = read_data("rowing.csv")
    total, fast, slow = calculate_stats(data)

    print(f"Total Distance: {total} meters")
    print(f"Fastest Pace: {fast}")
    print(f"Slowest Pace: {slow}")

if __name__ == "__main__":
    main()
