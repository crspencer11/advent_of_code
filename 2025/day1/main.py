file_path = "https://adventofcode.com/2025/day/1/input"

def find_password(file_path: str) -> int:
    start = 50
    password = 0
    with open(file_path) as f:
        for line in f:
            print(f)
            l_or_r = line[0]
            magnitude = int(line[1:])
            if l_or_r == "L":
                start -= magnitude
                if start == 0:
                    password += 1

    return password

find_password(file_path)

