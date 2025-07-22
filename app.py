# print hello world each ten seconds
import time
import sys

while True:
    print("Hello, World!")
    time.sleep(10)  # This is a simple script that prints "Hello, World!" every 10 seconds.
    sys.stdout.flush()  # Ensure the output is flushed immediately.
