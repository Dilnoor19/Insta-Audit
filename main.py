# "import" ka matlab: Python ke ready-made tools ko use karna.
# "json" module JSON files ko padhna aasan bana deta hai.
import json

followers_file_path = "followers_1.json"
following_file_path = "following.json"

with open(followers_file_path, "r",encoding="utf-8") as f: # encoding="utf-8" -> special characters (emoji, etc.) sahi dikhne ke liye
    followers_data = json.load(f)  # json.load(f) file ke andar ka data Python ki list/dict me badal deta hai

followers = set() # set() ek aisa dabba hai jisme duplicate nahi hote aur compare karna fast hota hai.
for item in followers_data:
    username = item["string_list_data"][0]["value"]
    followers.add(username) # set me username add karna

with open(following_file_path, "r",encoding="utf-8") as f:
    following_data = json.load(f)

following_list = following_data["relationships_following"]
following = set()
for item in following_list:
    username = item["title"]
    following.add(username) # set me username add karna


total_followers = len(followers)
total_following = len(following)

print("Total followers:", total_followers)
print("Total following:", total_following)

not_following_back = following - followers # set me order nahi hota. sorted() unhe A-Z order me list bana deta hai.
not_following_back = sorted(not_following_back)

print("Not following you back:", len(not_following_back))

with open("not_following_back.txt", "w", encoding="utf-8") as f:
    f.write("Total followers: " + str(total_followers) + "\n")
    f.write("Total following: " + str(total_following) + "\n\n")
    f.write("People who don't follow you back:\n\n")

    for name in not_following_back:
        f.write(name + "\n")

print("Done! not_following_back.txt file ban gayi.")