import os, logging
from pathlib import Path

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def generateTOC():
    pages = {}
    link = "https://CourtSC.github.io"
    logging.debug(link)

    # Create a new index.md file with links to the top-level subdirs in data.
    with open("index.md", "w") as index:
        for dir in os.listdir(".\\data"):
            if os.path.isdir(f".\\data\\{dir}"):
                index.write(f"[{dir}]({link}/data/{dir}/{dir}.html)")

    # Walk the data dir.
    for root, dirs, files in os.walk(".\\data", topdown=True):
        logging.debug(f"Root: {root}")
        logging.debug(f"Directories: {dirs}")
        logging.debug(f"Files: {files}")

        if len(files) > 0:
            dir = root.split("\\")[-1]
            with open(f"{root}\\{dir}.md", "w") as index:
                index.write(f"[Home]({link})\n")
                for file in files:
                    if Path(file).stem != dir:
                        index.write(
                            f"[{Path(file).stem}]({link}/{root[2:]}/{Path(file).stem}.html)\n"
                        )

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
        for key, val in pages.items():
            config.write(f" - {val[27:]}\\{key}.md\n")


if __name__ == "__main__":
    generateTOC()
