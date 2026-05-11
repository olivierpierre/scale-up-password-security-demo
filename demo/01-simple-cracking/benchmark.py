#!/usr/bin/env python3

import os
import re
import subprocess
import sys

import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({
    "font.size": 16,          # base font size
    "axes.titlesize": 20,     # plot title
    "axes.labelsize": 18,     # x/y labels
    "xtick.labelsize": 14,    # x ticks
    "ytick.labelsize": 14,    # y ticks
    "legend.fontsize": 14     # legend
})

# ============================================================
# Config
# ============================================================

HASHCAT_BIN = os.environ.get("HASHCAT_BINARY", "hashcat")
HASH_MODE = 0  # MD5

PASSWORD_LENGTHS = range(4, 13)

CHARSETS = {
    "digits": "0123456789",
    "lowercase": "abcdefghijklmnopqrstuvwxyz",
    "lower+digits": "abcdefghijklmnopqrstuvwxyz0123456789",
    "mixedcase+digits": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
}

# ============================================================
# Benchmark hashcat speed
# ============================================================

def run_hashcat_benchmark():
    print("[*] Running hashcat benchmark (MD5)...")

    cmd = [HASHCAT_BIN, "-m", str(HASH_MODE), "-b"]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    output = result.stdout + result.stderr

    match = re.search(
        r"Speed\.#\d+\.*:\s*([\d\.]+)\s*(GH/s|MH/s|kH/s|H/s)",
        output,
        re.IGNORECASE,
    )

    if not match:
        print(output)
        raise RuntimeError("Could not parse hashcat benchmark output")

    value = float(match.group(1))
    unit = match.group(2).lower()

    if unit == "gh/s":
        return value * 1e9
    if unit == "mh/s":
        return value * 1e6
    if unit == "kh/s":
        return value * 1e3
    return value


# ============================================================
# Time formatting
# ============================================================

def seconds_to_human(seconds):
    if seconds < 1:
        return f"{seconds*1000:.2f} ms"
    if seconds < 60:
        return f"{seconds:.2f} sec"
    if seconds < 3600:
        return f"{seconds/60:.2f} min"
    if seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    if seconds < 31536000:
        return f"{seconds/86400:.2f} days"
    return f"{seconds/31536000:.2f} years"


# ============================================================
# Model
# ============================================================

def estimate_time(charset_size, length, speed):
    keyspace = charset_size ** length
    avg_time = keyspace / (2 * speed)
    return keyspace, avg_time


# ============================================================
# Main
# ============================================================

def main():

    speed = run_hashcat_benchmark()
    print(f"[+] Speed: {speed:,.0f} H/s")

    results = []

    for name, charset in CHARSETS.items():
        for length in PASSWORD_LENGTHS:

            keyspace, t = estimate_time(len(charset), length, speed)

            results.append({
                "charset": name,
                "length": length,
                "time": t,
            })

    df = pd.DataFrame(results)

    # ========================================================
    # GRAPH 1: time vs password length
    # ========================================================

    plt.figure(figsize=(10, 6))

    for name in CHARSETS.keys():
        sub = df[df["charset"] == name]
        plt.plot(sub["length"], sub["time"], marker="o", label=name)

    plt.yscale("log")

    # clean human-readable ticks
    pretty_ticks = [
        1,
        60,
        3600,
        86400,
        31536000,
        3153600000,  # ~100 years
    ]

    plt.yticks(pretty_ticks, [seconds_to_human(t) for t in pretty_ticks])

    plt.xlabel("Password Length")
    plt.ylabel("Average Crack Time")
    plt.title("MD5 Crack Time vs Password Length")
    plt.grid(True)
    plt.legend()

    plt.savefig("length_vs_time.pdf", bbox_inches="tight")

if __name__ == "__main__":
    main()