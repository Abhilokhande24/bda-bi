#!/usr/bin/env python3
import sys

# Read input line by line
for line in sys.stdin:
    line = line.strip()  # Remove whitespace
    words = line.split()  # Split into words
    for word in words:
        print(f"{word}\t1")  # Emit (word, 1)

#!/usr/bin/env python3
import sys
from collections import defaultdict

word_count = defaultdict(int)

# Read input from standard input
for line in sys.stdin:
    word, count = line.strip().split("\t")
    word_count[word] += int(count)  # Aggregate counts

# Print the final word frequencies
for word, count in word_count.items():
    print(f"{word}\t{count}")
