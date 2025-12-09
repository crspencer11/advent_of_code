file_path = "day1/codes.txt"

def find_password(file_path: str) -> int:
    start = 50
    password = 0
    with open(file_path) as f:
        for line in f:
            stripped = line.strip()
            if not stripped:
                continue
            direction = stripped[0].upper()
            magnitude = int(stripped[1:])
            if direction == "L":
                start = (start - magnitude) % 100
            else:
                start = (start + magnitude) % 100
            if start == 0:
                password += 1
    return password

password = find_password(file_path)
print(password)