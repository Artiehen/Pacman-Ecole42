import sys
import json

from mazegenerator import MazeGenerator

# class CustomError(Exception):
#     pass


def remove_comments(text) -> str:
    """This function removes comments from config.json for
    proper json file handling"""
    lines = []

    for line in text.splitlines():
        in_string = False
        escaped = False
        output = []

        for char in line:
            if char == '"' and not escaped:
                in_string = not in_string

            if char == '#' and not in_string:
                break

            output.append(char)

            escaped = char == '\\' and not escaped

        lines.append(''.join(output))

    return '\n'.join(lines)


def main() -> None:
    """This is the main function"""

    if len(sys.argv) != 2:
        print("Please run game as 'python3 pac-man.py config.json'")
        sys.exit(1)

    try:
        with open("config.json") as f:
            text = f.read()
        data = json.loads(remove_comments(text))
        
        print(data)
        size = (data["width"], data["height"])

        maze_gen = MazeGenerator(size)
        # maze_gen.generate()

        maze = maze_gen.maze

        with open("test.txt", "w") as e:
            for row in maze:
                e.write("".join(f"{cell:X}" for cell in row) + "\n")


        data["h_score"] = json.dump


        # with open(data["h_score"], "w") as s:
        #     s.write("Testing score save")
        
        # display_maze(maze, False)

    except FileNotFoundError:
        print("Unable to locate config.json")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
