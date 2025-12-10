file_path = "day1/codes.txt"

def count_clicks(file_path: str) -> int:
    start = 50
    clicks = 0

    with open(file_path) as f:
        for line in f:
            stripped = line.strip()
            if not stripped:
                continue
            direction = stripped[0].upper()
            magnitude = int(stripped[1:])
            if direction == "L":
                temp = start % 100
                if temp == 0:
                    temp = 100
                if magnitude >= temp:
                    clicks += 1 + (magnitude - temp) // 100
                start = (start - magnitude) % 100
            else:
                temp = (100 - start) % 100
                if temp == 0:
                    temp = 100
                if magnitude >= temp:
                    clicks += 1 + (magnitude - temp) // 100
                start = (start + magnitude) % 100

    return clicks

clicks = count_clicks(file_path)
print(clicks)
