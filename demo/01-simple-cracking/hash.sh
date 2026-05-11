#!/usr/bin/env bash
set -euo pipefail

INPUT="rockyou.txt"
OUTPUT="rockyou_md5.txt"

> "$OUTPUT"

echo "[*] Hashing lines with MD5..."

while IFS= read -r line; do
    # compute md5 of the line (no newline included)
    echo -n "$line" | md5sum | awk '{print $1}' >> "$OUTPUT"
done < "$INPUT"

echo "[+] Done: $OUTPUT"
