import csv
import json
from typing import List, Dict, Tuple


def parse_file(filename: str) -> List[dict]:
    result = []
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='|')
        for row in list(reader)[1:]:
            item = {
                'lastname': row[0],
                'name': row[1],
                'patronymic': row[2],
                'date_of_birth': row[3],
                'id': row[4]
            }
            result.append(item)

    return result


def get_unique_records(data: List[dict]):
    row_data = list(set([json.dumps(item) for item in data]))
    return [json.loads(item) for item in row_data]


def get_duplicates(data: List[dict]) -> List[dict]:
    hash: Dict[str, dict] = {}
    result = []

    for record in data:
        if record['id'] not in hash:
            hash[record['id']] = record

        elif record['id'] in hash and hash.get(record['id']) != record:
            result.append(record)

    return result


def main(filename: str) -> Tuple[list, list]:
    data = parse_file(filename)
    unique = get_unique_records(data)
    duplicates = get_duplicates(data)
    return unique, duplicates


if __name__ == '__main__':
    unique, duplicates = main('data.csv')
    print('unique:')
    [print(item) for item in unique]
    print()
    print('duplicates')
    [print(item) for item in duplicates]
