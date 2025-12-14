file_path = "day2/data.txt"

def find_invalid_identifiers(file_path: str) -> int:
    with open(file_path) as file:
        for i in range(len(file)):
            print(i)
    return 0

find_invalid_identifiers(file_path)
