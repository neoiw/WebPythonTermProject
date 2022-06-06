import os
import csv

def grab():
    user_token = input("Your Discord user token: ")
    channel_id = input("Discord channel ID: ")
    os.system('cmd /c "dotnet .\\DiscordChatExporter.CLI\\DiscordChatExporter.Cli.dll export -t "{0}" -c {1} -f "CSV" -o "output.csv"'.format(user_token,channel_id))


def analyze():
    with open("output.csv", encoding='utf-8') as csv_file:
        cr = csv.reader(csv_file, delimiter=",")
        
        count = {}

        for line in cr:
            if line[1] == "Author":
                continue
            if line[1] not in count.keys():
                count[line[1]]=1
                continue
            if line[1] in count.keys():
                count[line[1]] += 1
    
        print(count)



if __name__ == '__main__':
    #grab()
    analyze()