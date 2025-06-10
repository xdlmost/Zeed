import os
import tarfile

class PackageMaker:
    @staticmethod
    def make_tar_gz(zeed_name:str, input_dir: str, output_dir: str):
        tar_gz_file = os.path.join(output_dir,zeed_name)
        with tarfile.open(tar_gz_file, "w:gz") as tar:
            for root, dirs, files in os.walk(input_dir):
                for file in files:
                    tar.add(os.path.join(root, file), arcname=os.path.relpath(os.path.join(root, file), input_dir))
        return tar_gz_file