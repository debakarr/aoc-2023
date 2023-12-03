from collections import namedtuple


class CubeSet(namedtuple("CubeSet", "red blue green", defaults=(0, 0, 0))):
    def met_constraint(self, other: "CubeSet") -> bool:
        return (
            self.red <= other.red
            and self.green <= other.green
            and self.blue <= other.blue
        )

    def __repr__(self) -> str:
        return f"CubeSet(red={self.red}, green={self.green}, blue={self.blue})"


contraints = CubeSet(red=12, green=13, blue=14)


def make_cubeset(string):
    items = string.split(",")
    items = [item.strip().split() for item in items]
    cube_count = {cube: int(count) for (count, cube) in items}
    return CubeSet(**cube_count)
