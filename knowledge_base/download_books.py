import os
from pathlib import Path

import requests
from tqdm import tqdm
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))
from config.constants import BOOK_URLS


RAW_BOOK_DIR = Path("data/raw_books")
RAW_BOOK_DIR.mkdir(parents=True, exist_ok=True)


def download_file(url: str):
    filename = url.split("/")[-1]
    filepath = RAW_BOOK_DIR / filename

    if filepath.exists():
        print(f"✓ Already exists: {filename}")
        return

    print(f"Downloading {filename}")

    response = requests.get(url, stream=True)
    response.raise_for_status()

    total_size = int(response.headers.get("content-length", 0))

    with open(filepath, "wb") as file:
        with tqdm(
            total=total_size,
            unit="B",
            unit_scale=True,
            desc=filename,
        ) as progress_bar:

            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    progress_bar.update(len(chunk))

    print(f"✓ Saved → {filepath}")


def download_all_books():
    for url in BOOK_URLS:
        try:
            download_file(url)
        except Exception as e:
            print(f"Failed: {url}")
            print(e)


if __name__ == "__main__":
    download_all_books()
