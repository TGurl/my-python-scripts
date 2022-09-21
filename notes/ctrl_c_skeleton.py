import signal
import time


def handler(signum, frame):
    valid = ["y", "n", "yes", "no"]
    res = input(" Ctrl-c was pressed. Do you really want to exit? (y/n) ").lower()
    if res in valid:
        if res in ["y", "yes"]:
            exit(1)
    else:
        return True


signal.signal(signal.SIGINT, handler)

count = 0
while True:
    print(count)
    count += 1
    time.sleep(0.1)
