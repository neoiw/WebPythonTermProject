import os

def grab():
    user_token = input("Your Discord user token: ")
    channel_id = input("Discord channel ID: ")
    os.system('cmd /c "dotnet .\\DiscordChatExporter.CLI\\DiscordChatExporter.Cli.dll export -t "{0}" -c {1} -f "PlainText" -o "output.txt"'.format(user_token,channel_id))


def analyze():
    file = open(".\\output.txt")

    raw_data = file.readlines
    

if __name__ == '__main__':
    grab()