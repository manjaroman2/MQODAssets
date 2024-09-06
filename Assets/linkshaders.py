from os import symlink
from pathlib import Path

projpath = Path(__file__).parent.parent
print(projpath.absolute())
for x in projpath.glob("./Temp/*.shader"):
    symlink(x, projpath / "Assets" / str(x).split("-")[-1])
    print(str(x).split("-")[-1])
