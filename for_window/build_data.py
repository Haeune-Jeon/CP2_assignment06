"""
build_data.py

이 모듈은 연도별 csv 파일을 읽어 데이터를 처리하고 저장하는 기능을 제공합니다.

함수:
- build_data(): CSV 파일을 읽어 데이터 구조로 변환하여 반환합니다.
- print_data(data): 데이터를 화면에 출력합니다.

직접 실행 시:
- 모듈이 직접 실행될 경우, 'build_data()'를 호출하여 처리된 데이터를 출력합니다.

모듈로 사용 시:
- build_data()와 print_data() 함수를 다른 파일에서 import하여 사용할 수 있습니다.
"""

import csv

def build_data():
    """
    입력한 연도(2020 ~ 2023)의 CSV 파일을 읽어 데이터를 처리하여 반환합니다.

    반환 형식:
    {
        "key1": {
            "subkey1": [int, int],
            "subkey2": [int, int],
            ...
        },
        ...
    }
    """
    data = {}

    while True:
        year_input = input("연도 선택(2020, 2021, 2022, 2023) : ")
        if year_input in ['2020', '2021', '2022', '2023']:
            break
        else:
            print("잘못된 입력입니다.")

    input_file = year_input + '1231.csv'
    f = open(input_file, 'r', encoding = 'euc-kr')
    reader = csv.reader(f)

    next(reader)

    for line in reader:
        if line[1] not in data:
            data[line[1]] = {}
        data[line[1]][int(line[2].strip())] = [int(line[3]),int(line[4])]
    
    f.close()
    return data

def print_data(data):
    """
    데이터를 화면에 출력합니다.

    매개변수:
    - data: build_data() 함수에서 반환된 데이터 구조
    """
    print(data)

if __name__ == "__main__":
    """
    파일이 직접 실행될 경우 실행되는 코드 블록입니다.
    1. 'build_data()'를 호출하여 데이터를 처리합니다.
    2. 처리된 데이터를 print_data()를 통해 출력합니다.
    """
    print("build_data 모듈입니다.")
    print("main 함수를 실행중입니다...\n")
    print_data(build_data())