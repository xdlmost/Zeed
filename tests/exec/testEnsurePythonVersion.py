from zeed.FileSystem import FileSystem
from zeed.Node import Node
import os

def _main(zeed_file_path: str):
    fs = FileSystem(zeed_file_path)
    zeed_node = Node(fs)
    zeed_node.prepare()


if __name__ == "__main__":
    zeed_file_path = os.path.join(os.path.dirname(__file__), "Zeedfile")
    with open(zeed_file_path, "w") as f:
        f.write("""
EnsurePythonVersion("3.10")
Zeed("123")
Zeed("456")
Zeed("789")
Zeed("101")
Zeed("112")
Zeed("123")
Zeed("134")
env = Environment()
print(env.zeeds)
""")

    _main(zeed_file_path)

    os.remove(zeed_file_path)