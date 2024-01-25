#!/usr/bin/python3
for num in range(100):
    if (num < 10):
        print(f"{num:02d}", end=", ")
        continue
    print(f"{num}", end=", " if num < 99 else "\n")
