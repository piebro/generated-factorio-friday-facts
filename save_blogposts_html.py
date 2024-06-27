import sys
import requests
from pathlib import Path


def save_factorio_blogpost_html(start_post, end_post):
    base_url = "https://factorio.com/blog/post/fff-"
    save_dir = Path("fff_html")
    save_dir.mkdir(exist_ok=True)

    for post_number in range(start_post, end_post + 1):
        url = f"{base_url}{post_number}"
        response = requests.get(url)

        if response.status_code == 200:
            filepath = save_dir / f"fff_{post_number}.html"

            # Decode the content to a string
            content = response.content.decode("utf-8")

            with filepath.open("w", encoding="utf-8") as f:
                f.write(content)

            print(f"Saved post {post_number}")
        else:
            print(f"Failed to retrieve post {post_number}")


save_factorio_blogpost_html(int(sys.argv[1]), int(sys.argv[2]))
