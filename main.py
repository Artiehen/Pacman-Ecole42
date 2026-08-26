import sys

def main() -> None:

    if len(sys.argv) != 2:
        print("Please run game as 'python3 pac-man.py config.json'")
        sys.exit(1)
    else:
        print("Yes")
    


if __name__ == "__main__":
    main()
