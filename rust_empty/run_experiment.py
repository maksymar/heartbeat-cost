#! /usr/bin/python3
import re
import csv
import time
import datetime as dt
import subprocess


BALANCE_PATTERN = re.compile('.+Balance: ([0-9_]*)')


def balance(canister):
    '''
        Extract balance from command
        `$ dfx canister status CANISTER_NAME`
    '''
    # Run subprocess.
    p = subprocess.Popen(
        ['dfx', 'canister', 'status', canister],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    _, err = p.communicate()

    # Decode, convert multiline into a single line.
    text = err.decode("utf-8")
    text = ''.join(text.splitlines())

    # Extract balance value.
    m = BALANCE_PATTERN.match(text)
    if m:
        return int(m.group(1).replace('_', ''))


def run_experiment(canister, total_duration, pause_sec):
    data = []

    start = 'init'
    while True:
        current_balance = balance(canister)

        if start == 'init':
            start = dt.datetime.now()
            init_balance = current_balance
        else:
            elapsed = dt.datetime.now() - start
            elapsed_sec = round(elapsed.total_seconds(), 1)
            burned = int(init_balance - current_balance)
            burn_rate = int(burned / elapsed_sec)
            burn_rate_tc_year = round(
                60 * 60 * 24 * 365 * burn_rate / 1_000_000_000_000, 1)

            data.append({
                'time, s': elapsed_sec,
                'burned, Cycles': burned,
                'burn rate, Cycles/s': burn_rate,
                'burn rate, TCycles/y': burn_rate_tc_year,
            })

            # Output progress.
            burned_mc = round(burned / 1_000_000, 1)
            burn_rate_mc_sec = round(burn_rate / 1_000_000, 1)
            print(
                f'{elapsed_sec} s, {burned_mc} MC, {burn_rate_mc_sec} MC/s, {burn_rate_tc_year} TC/y')

            if total_duration <= elapsed:
                break

        time.sleep(pause_sec)

    return data


def main():
    canister = 'rust_backend'
    total_duration = dt.timedelta(minutes=15)
    pause_sec = 60
    csv_file = './data.csv'
    csv_delimiter = ';'

    data = run_experiment(canister, total_duration, pause_sec)

    # Save CSV data.
    if len(data) > 0:
        with open(csv_file, 'w') as f:
            w = csv.DictWriter(f, data[0].keys(), delimiter=csv_delimiter)
            w.writeheader()
            w.writerows(data)


if __name__ == '__main__':
    main()
