import sys

interval_list = sys.stdin.readline().split(",")
intervals = [tuple(map(int, item.split("-"))) for item in interval_list]
