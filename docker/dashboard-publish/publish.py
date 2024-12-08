import zipfile
import os
import sys
import uuid
import glob
import shutil

exports_dir = os.getenv("EXPORTS_DIR", "/tmp/exports")
expand_dir = f"/tmp/{uuid.uuid4()}"
expand_dir = exports_dir
JFROG_USER = os.getenv("JFROG_USER")
JFROG_PASSWORD = os.getenv("JFROG_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")

files = os.listdir(exports_dir)
os.makedirs(expand_dir, exist_ok=True)


def expand_zip(zip_file, target_dir):
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(target_dir)


def zip_directory(directory_path, zip_path):
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                zipf.write(
                    os.path.join(root, file),
                    os.path.relpath(
                        os.path.join(root, file),
                        os.path.join(directory_path, ".."),
                    ),
                )


def change_dbs_url(dir):
    for file_name in glob.glob(f"{dir}/*", recursive=True):
        with open(file_name, "r") as file:
            lines = file.readlines()

        with open(file_name, "w") as file:
            for line in lines:
                if line.startswith("sqlalchemy_uri"):
                    file.write(
                        f"sqlalchemy_uri: postgresql+psycopg2://{JFROG_USER}:{JFROG_PASSWORD}@{DATABASE_HOST}:5432/jfrog\n"
                    )
                else:
                    file.write(line)

        file.close()


for file in files:
    file_name = None
    if file.endswith(".zip"):
        expand_zip(os.path.join(exports_dir, file), expand_dir)
        file_name = file.split(".")[0]
    else:
        continue

    db_dir_name = None
    for directory_name in glob.glob(f"{expand_dir}/**/*", recursive=True):
        if (
            os.path.isdir(directory_name)
            and os.path.basename(directory_name) == "databases"
        ):
            change_dbs_url(directory_name)
            db_dir_name = directory_name

    parent_directory = os.path.dirname(db_dir_name)
    zip_directory(
        parent_directory,
        expand_dir + f"/{file_name}.zip",
    )

    shutil.rmtree(parent_directory)
