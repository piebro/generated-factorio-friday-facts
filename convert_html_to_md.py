import sys
import os
from bs4 import BeautifulSoup
import re
import html2text


def preprocess_html(content, post_number):
    soup = BeautifulSoup(content, "html.parser")

    # Replace video elements
    for video in soup.find_all("video"):
        video_source = video.find("source")
        video_filename = ".".join(
            video_source.get("src", "source").split("/")[-1].split(".")[:-1]
        )
        video.replace_with(f"*video {video_filename}*")

    # Replace image elements, including those within anchor tags
    image_counter = 1
    for a_tag in soup.find_all("a", href=True):
        img = a_tag.find("img")
        if img:
            img_filename = ".".join(
                img.get("src", "image").split("/")[-1].split(".")[:-1]
            )
            a_tag.replace_with(f"*Image {img_filename}*")
            image_counter += 1

    # Replace standalone image elements
    for img in soup.find_all("img"):
        img_filename = ".".join(img.get("src", "image").split("/")[-1].split(".")[:-1])
        img.replace_with(f"*Image {img_filename}*")
        image_counter += 1

    return str(soup)


def process_factorio_blog(start_post, end_post):
    input_folder = "fff_html"
    output_folder = "fff_markdown"
    os.makedirs(output_folder, exist_ok=True)

    for post_number in range(start_post, end_post + 1):
        input_file = os.path.join(input_folder, f"fff_{post_number}.html")
        if os.path.exists(input_file):
            with open(input_file, "r", encoding="utf-8") as f:
                content = f.read()

                # Preprocess HTML
                preprocessed_content = preprocess_html(content, post_number)
                soup = BeautifulSoup(preprocessed_content, "html.parser")

                title = soup.find("h2").text.strip()
                blog_content = soup.find("div", class_="panel-inset-lighter")

                # Convert HTML to Markdown
                h = html2text.HTML2Text()
                markdown_content = h.handle(str(blog_content))

                # Clean up the Markdown content
                markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)

                # Save to file
                output_file = os.path.join(output_folder, f"fff_{post_number}.md")
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(f"# {title}\n\n")
                    f.write(markdown_content)

                print(f"Processed post {post_number}: {title}")
        else:
            print(f"File not found for post {post_number}")


process_factorio_blog(int(sys.argv[1]), int(sys.argv[2]))
