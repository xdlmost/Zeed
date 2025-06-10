from zeed.Utils.FileSystem import FileSystem
from zeed.Node import Node
import os

def _main(zeed_file_path: str):
    zeed_node = Node(zeed_file_path)
    zeed_node.prepare()


if __name__ == "__main__":
    zeed_file_path = os.path.join(os.path.dirname(__file__), "Zeedfile")
    with open(zeed_file_path, "w") as f:
        f.write("""
from pathlib import Path    
EnsurePythonVersion("3.10")
EnsureZeedVersion("0.1.0")

hehe_zeed = Zeed(name="hehe", version="1.0.0", platform=None)
hehe_template_dir = hehe_zeed.add_dir(path="template")
hehe_template_a_dir = hehe_template_dir.add_dir(path="a")
hehe_template_a_dir.add_blob_rule(from_dir=Path("template")/"a", files_filter="hehe")
env = Environment()
print(env.get_dict())
                
print(GetDict())

""")

    _main(zeed_file_path)

    os.remove(zeed_file_path)