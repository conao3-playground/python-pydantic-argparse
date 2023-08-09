import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', type=int, default=42)
    parser.add_argument('--bar')

    return parser.parse_args()


def main():
    args = parse_args()
    print(args)
