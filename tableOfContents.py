import os, logging
from pathlib import Path

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def generateTOC():
    pages = {}
    link = "https://CourtSC.github.io/"
    logging.debug(link)
    for root, dirs, files in os.walk(".\data", topdown=True):
        logging.debug(f"Root: {root}")
        logging.debug(f"Directories: {dirs}")
        logging.debug(f"Files: {files}")

        for file in files:
            if Path(file).suffix == ".md":
                pages[Path(file).stem] = f"{link}/{root[2:]}/{Path(file).stem}.html"

    logging.debug(f"Pages: {pages}")

    with open("index.md", "w") as index:
        for key, val in pages.items():
            index.write(f"[{key}]({val})")

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
            config.write(f" - {val[27:]}\\{key}.md")


if __name__ == "__main__":
    generateTOC()
