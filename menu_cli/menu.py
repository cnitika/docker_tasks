def main():
    while True:
        print("1. Say Hello")
        print("2. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            print("Hello from Docker!")
        elif choice == "2":
            break

if __name__ == '__main__':
    main()