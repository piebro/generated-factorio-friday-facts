import argparse
from pathlib import Path
import re
from anthropic import Anthropic


def merge_markdown_files(file_numbers, folder_path):
    merged_content = ""
    for i in file_numbers:
        file_path = folder_path / f"fff_{i}.md"
        if file_path.exists():
            with file_path.open("r", encoding="utf-8") as file:
                merged_content += f"<example>\n{file.read()}\n</example>"
    return merged_content


def create_prompt(merged_content, blogpost_number, bullet_points):
    if len(bullet_points) == 0:
        more_instruction = "Choose a topic similiar to the exmaples blogposts."
    elif len(bullet_points) == 1:
        more_instruction = f"The blogpost should be about: {bullet_points[0]}."
    else:
        bullet_points_str = "\n".join(f"- {point}" for point in bullet_points)
        more_instruction = (
            f"The blogpost should be about the following items:\n{bullet_points_str}\n"
        )

    prompt = f"""<prompt>
<examples>
{merged_content}
</examples>
<instructions>
Based on these examples, write a new blogpost for the game factorio with the number {blogpost_number} in a similar style. Write only the blogpost, without an introduction or an explanation like "Here's a new Factorio blogpost ...". {more_instruction}
</instructions>
</prompt>
"""
    return prompt


def generate_blogpost(prompt):
    client = Anthropic()
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=2000,
        system="You are a developer of Factorio with a passion for writing and technical blogposts about games. Your task is to write similar to the style in the given examples.",
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content


def save_generated_content(content, folder_path, command):
    folder_path.mkdir(exist_ok=True)
    next_num = len(list(folder_path.iterdir()))

    title_match = re.search(r"^# Friday Facts #(\d+) - (.+)$", content, re.MULTILINE)
    if title_match:
        blogpost_num = title_match.group(1)
        title = title_match.group(2)
        # Convert title to filename-friendly format
        title_slug = re.sub(r"[^\w\-]", "-", title).strip("-").lower()
        file_name = f"{next_num:03d}-fff-{blogpost_num}-{title_slug}.md"
    else:
        file_name = f"{next_num:03d}-fff.md"

    file_path = folder_path / file_name
    with open(file_path, "w", encoding="utf-8") as outfile:
        outfile.write(f"<!-- Command for generating this post: {command} -->\n\n")
        outfile.write(content)
    print(f"Generated content saved as {file_path}")


def get_command_string(args):
    commands = [
        "python create_new_blogpost.py",
        f"--blogpost_number {str(args.blogpost_number)}",
        f"--prev_blogpost_as_examples {' '.join(map(str, args.prev_blogpost_as_examples))}",
    ]
    if len(args.bullet_points) > 0:
        bullet_points = [f'"{bp}"' for bp in args.bullet_points]
        commands.append(f"--bullet_points {' '.join(bullet_points)}")

    return " ".join(commands)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a blogpost based on example files and bullet points."
    )
    parser.add_argument(
        "--blogpost_number", type=int, required=True, help="Number of the blogpost"
    )
    parser.add_argument(
        "--prev_blogpost_as_examples",
        type=int,
        nargs="+",
        required=True,
        help="List of file numbers to use as examples",
    )
    parser.add_argument(
        "--bullet_points",
        type=str,
        nargs="+",
        default=[],
        help="List of bullet points for the blogpost",
    )
    args = parser.parse_args()

    merged_content = merge_markdown_files(
        args.prev_blogpost_as_examples, Path("fff_markdown")
    )
    prompt = create_prompt(merged_content, args.blogpost_number, args.bullet_points)
    generated_blogpost = generate_blogpost(prompt)[0].text
    save_generated_content(
        generated_blogpost, Path("fff_generated"), get_command_string(args)
    )


if __name__ == "__main__":
    main()
