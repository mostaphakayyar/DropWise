from dropwise.loops import create_loop

def main():
    title = input("What do you need to do? ")
    loop = create_loop(title)
    print(f"Loop created: {loop['title']}")


if __name__ == "__main__":
    main()