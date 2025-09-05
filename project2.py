import sqlite3

con = sqlite3.connect("youtube_videos.db")

cursor = con.cursor()

cursor.execute(
    """ 
             CREATE TABLE IF NOT EXISTS Videos(
                 id INTEGER  PRIMARY KEY,
                 Name TEXT NOT NULL,
                 time TEXT NOT NULL
             )  
               
               """
)



def list_videos():
    print("\n")
    print("-" * 70)
    # print("ID  |           NAME          |       TIME      ")
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
    print("\n")
    print("-" * 70)


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)", (name, time))
    con.commit()


def update_video(video_id, new_name, new_time):
    cursor.execute(
        "UPDATE videos SET name = ? ,time = ?  where  id = ?",
        (new_name, new_time, video_id),
    )
    con.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id  = ?", (video_id,))
    con.commit()


def main():
    while True:

        print("\n Youtbe Manager app with Db")
        print("1. list all youtube videos")
        print("2. Add a youtube videos")
        print("3 Update a Youtube video ")
        print("4. Delete a youtube video")
        print("5 Exit the app ")

        choice = input("Enter Your Choice: ")
        match choice:
            case "1":
                list_videos()
            case "2":
                name = input("Enter the video name : ")
                time = input("Enter the video length : ")
                add_video(name, time)
            case "3":
                video_id = int(input("Enter the video ID to update : "))
                name = input("Enter the video name : ")
                time = input("Enter the Video time : ")

                update_video(video_id, name, time)
            case "4":
                video_id = int(input("Enter the video ID to delete : "))

                delete_video(video_id)
            case "5":
                break
            case _:
                print("Invalid Choice ")

    con.close()


if __name__ == "__main__":
    main()
