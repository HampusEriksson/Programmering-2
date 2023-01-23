from dataclasses import dataclass


@dataclass
class ClassName:
    def __str__(self) -> str:
        pass


class ClassName:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        pass
