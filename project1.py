import json


def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file, indent=4)


def list_all_videos(videos):
    if not videos:
        print("No videos found.")
    else:
        for index, video in enumerate(videos, start=1):
            print(f"{index}. {video['name']} ({video['time']})")


def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
    print("✅ Video added successfully!")


def update_video(videos):
    list_all_videos(videos)
    try:
        choice = int(input("Enter video number to update: ")) - 1
        if 0 <= choice < len(videos):
            name = input("Enter new video name: ")
            time = input("Enter new video time: ")
            videos[choice] = {"name": name, "time": time}
            save_data_helper(videos)
            print("✅ Video updated successfully!")
        else:
            print("❌ Invalid video number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def delete_video(videos):
    list_all_videos(videos)
    try:
        choice = int(input("Enter video number to delete: ")) - 1
        if 0 <= choice < len(videos):
            deleted = videos.pop(choice)
            save_data_helper(videos)
            print(f"✅ Deleted video: {deleted['name']}")
        else:
            print("❌ Invalid video number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def main():
    videos = load_data()
    while True:
        print("\n!! YouTube Manager !!")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("👋 Exiting... Bye!")
                break
            case _:
                print("❌ Invalid choice. Please try again.")



if __name__ == "__main__":
    main()

