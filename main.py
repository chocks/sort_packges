from enum import Enum

BULK_VOLUME = 1_000_000
PER_DIMENSION_MAX = 150
BULK_MASS = 20


class PackageSorter:
    def __init__(self, width: int, height: int, length: int, mass: int) -> None:
        self.width = width
        self.height = height
        self.length = length
        self.mass = mass

    class Stack(Enum):
        STANDARD = 1
        SPECIAL = 2
        REJECTED = 3

    def _is_bulk(self):
        if self.width * self.height * self.length >= BULK_VOLUME or (
            self.length >= PER_DIMENSION_MAX
            or self.width >= PER_DIMENSION_MAX
            or self.height >= PER_DIMENSION_MAX
        ):
            return True
        return False

    def _is_heavy(self):
        return self.mass >= BULK_MASS

    def get_stack(self):
        is_bulk = self._is_bulk()
        is_heavy = self._is_heavy()
        stack = None

        if is_bulk and is_heavy:
            stack = self.Stack(3)
        elif is_bulk or is_heavy:
            stack = self.Stack(2)
        else:
            stack = self.Stack(1)

        return stack.name


def sort(width: int, height: int, length: int, mass: int) -> str:
    if width < 0 or height < 0 or length < 0 or mass < 0:
        raise ValueError('Invalid data')
    ps = PackageSorter(width, height, length, mass)
    return ps.get_stack()


if __name__ == "__main__":
    print(sort(10, 10, 10, 10))