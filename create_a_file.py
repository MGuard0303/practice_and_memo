import os
import pathlib


path = "C:/test/test_file.txt"  # Windows path
content = "THIS IS A TEST FILE" * 3

with open(path, "w") as f:
  for i in range(20):
    f.write(content + "\n")
