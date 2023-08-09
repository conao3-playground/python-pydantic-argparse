import argparse
from typing import Optional

import pydantic


class Args(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(from_attributes=True)

    foo: int = 42
    bar: Optional[str]


def parse_args() -> Args:
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', type=int, default=42)
    parser.add_argument('--bar')

    return Args.model_validate(parser.parse_args())


def main():
    args = parse_args()
    print(args)
