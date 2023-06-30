#!/usr/bin/env python3

import argparse
import math
import os
import struct
import sys
import time


class Pipetime:
    def play(fd, filename, *, max_pause=-1, speed=1):
        with open(filename, "rb") as f:
            while True:
                data = f.read(4)
                if not data:
                    break
                l = struct.unpack("!i", data)[0]
                data = f.read(l)
                os.write(fd, data)
                pause_ms = struct.unpack("!i", f.read(4))[0]
                pause_ms /= speed
                if max_pause >= 0:
                    pause_ms = min(pause_ms, max_pause * 1000)
                time.sleep(pause_ms / 1000)

    def record(fd, fdout, filename):
        with open(filename, "wb") as f:
            part = b""
            start = time.time()
            data = ["start"]
            while data:
                data = os.read(fd, 1)
                elapsed = time.time() - start
                run = data

                if not data or elapsed > 0.01:  # more than 10ms
                    f.write(struct.pack("!i", len(part)))  # pack 4byte long
                    f.write(part)
                    f.write(struct.pack("!i", int(math.floor(elapsed * 1000))))

                    if not data:
                        break

                    part = b""
                    start = time.time()

                os.write(fdout, data)
                part += data


def main(parser):
    args = parser.parse_args()

    if args.record:
        fd = sys.stdin.fileno()
        if sys.stdin.isatty():
            print("tty is not supported")
            return 1
        Pipetime.record(fd, sys.stdout.fileno(), args.file)
    else:
        Pipetime.play(
            sys.stdout.fileno(), args.file, max_pause=args.max_pause, speed=args.speed
        )

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f"pipevcr - the linux pipe recorder")

    parser.add_argument("file", metavar="FILE", type=str, help="data file")
    parser.add_argument("-r", "--record", action="store_true", help="record pipe")
    parser.add_argument(
        "-s",
        "--speed",
        action="store",
        type=float,
        default=1,
        help="playback speed, <1 to slow down, >1 to speed up",
    )
    parser.add_argument(
        "-m",
        "--max-pause",
        action="store",
        type=float,
        default=-1,
        help="max pause time between outputs in seconds",
    )

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
    else:
        try:
            sys.exit(main(parser))
        except KeyboardInterrupt:
            print("aborted")
            sys.exit(1)
