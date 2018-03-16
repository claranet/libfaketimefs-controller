import collections
import datetime
import os
import time


FAKETIME_REALTIME_FILE = os.environ.get('FAKETIME_REALTIME_FILE')

Command = collections.namedtuple('Command', 'ref, time1, time2, rate')


def calculate_fake_time(command):
    # TODO: calculate the fake timestamp from command
    raise NotImplementedError


def calculate_status(command):
    # TODO: calculate status (MOVING or IDLE) from command
    raise NotImplementedError


def create_command(ref, time1, time2, rate):
    # TODO: create command namedtupe fro
    raise NotImplementedError


def get_time():
    if FAKETIME_REALTIME_FILE:
        with open(FAKETIME_REALTIME_FILE) as open_file:
            return float(open_file.read())
    else:
        return time.time()


def read_commands(table):
    # TODO: read and stream commands from DynamoDB
    raise NotImplementedError


def log_command(command):
    print('[{}] {}'.format(datetime.datetime.now(), command))


def send_command(command, table):
    log_command(command)
    # TODO: write command to DynamoDB
    raise NotImplementedError


def write_command(command, path):
    log_command(command)
    with open(path, 'w') as open_file:
        open_file.write(command)
