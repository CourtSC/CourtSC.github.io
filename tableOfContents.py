import os, logging
from pathlib import Path

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def generateTOC():
    pages = []
    for root, dirs, files in os.walk(".\data", topdown=True):
        logging.debug(f"Root: {root}")
        logging.debug(f"Directories: {dirs}")
        logging.debug(f"Files: {files}")

        for file in files:
            if Path(file).suffix == ".md":
                pages.append(f"{root[2:]}\\{file}")
                logging.debug(f"{file} added to Pages.")

    logging.debug(f"Pages: {pages}")

    with open("_config.yml", "w") as config:
        config.write(
            """
plugins:
  - jekyll-relative-links
relative_links:
  enabled: true
  collections: true
include:
"""
        )
        for page in pages:
            config.write(f" - {page}")


if __name__ == "__main__":
    generateTOC()
