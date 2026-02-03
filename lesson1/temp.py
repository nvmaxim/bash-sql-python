# Front Как, не используя методы списков и строк, по числу n построить число, в котором n записано 100 раз подряд (например, из n = 15 получить 1515...15 100 раз), а затем вывести это число и его квадрат?

import sys
import io


def get_algo_logic(n: int) -> tuple[str, str]:
    x = 0
    len_n = 0
    temp = n
    while temp > 0:
        len_n += 1
        temp //= 10
    power = 10**len_n
    for _ in range(100):
        x = x * power + n
    return str(x), str(x * x)


def solve(data_input: str) -> None:
    if not data_input:
        return
    try:
        input_data = data_input.split()
        n = int(input_data[0])
        number, square = get_algo_logic(n)
        sys.stdout.write(number + "\n")
        sys.stdout.write(square + "\n")
    except Exception:
        pass


def main():
    IS_LOCAL_TEST = True
    if IS_LOCAL_TEST:
        raw_data = 15
        input_steam = io.StringIO(raw_data).read
    else:
        input_steam = sys.stdin.read()
    solve(input_steam)


if __name__ == "__main__":
    main()
