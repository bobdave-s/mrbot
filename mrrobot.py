import colorama
from colorama import Fore
print("Chat with mr robot and ask him any question he must aswer you....")
mask =r'''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣐⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠉⠉⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⣠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⢀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡖⢾⠋⠀⠀⠀⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⣇⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠒⠒⠒⠒⠒⠒⠲⠲⠚⠓⠒⠒⠛⠓⢒⣖⠒⠒⠒⠒⠒⠒⢲⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⢠⠖⠋⠉⠷⣄⠀⠀⢠⠖⠉⡉⠑⢦⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠉⢻⠀⠀⠀⠀⣿⣾⣿⣦⡀⢸⠀⠀⢿⣿⣿⣷⡀⢸⠀⠀⠀⠀⢸⠋⠙⡇⠀⠀⠂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⠀⣀⠀⠀⠘⢿⣿⢟⣂⠞⠀⠀⠈⠿⣿⣿⣡⠞⠀⠀⠀⠀⢸⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⣾⠉⠉⠙⢧⡀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⣠⠞⠉⠉⡙⣇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣻⠀⠀⠀⠀⠙⢦⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣁⣀⣠⠞⠁⠀⠀⠀⠇⡏⠃⠀⠀⢀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⡤⣤⣤⣤⣤⣤⣤⣤⣤⣤⢤⠤⠤⠤⠤⢤⣤⣥⣤⣤⣤⣤⡤⢤⣤⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠛⠦⣄⡀⣀⣿⡛⣛⣛⣛⢛⢛⢛⣷⣀⣀⣴⣛⡛⠶⡄⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⣿⣩⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⢭⡉⡇⠀⠸⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⣿⣽⠀⠀⣶⡆⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⢠⣇⡇⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠘⢦⣰⣿⣿⠀⢰⡿⡇⣄⠀⠀⠀⠀⣼⣇⣠⠀⠀⢸⣿⣇⣠⠞⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡃⠀⠀⢠⠟⣿⣿⠤⠾⠀⢻⠛⡄⢰⠤⠽⠏⣿⡟⡷⠶⢼⡿⡟⢖⢄⠀⠈⣣⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠛⠦⣴⠏⠀⣿⣼⠀⠀⠀⠀⠀⢻⡞⠀⠀⠀⠻⠇⠀⠀⠀⡇⡇⠈⢷⡴⠚⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡴⠿⢦⣀⡾⠁⠀⠀⣿⢾⣀⣀⣀⣀⣀⣀⣁⣀⣀⣀⣀⣀⣀⣀⣠⣷⡇⠀⠈⠻⣄⡰⠾⠶⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣤⡴⣟⠀⠀⠀⣹⠀⠀⠀⠰⣿⣈⡿⢯⡉⣿⣿⣿⣿⣿⣿⣿⣿⡏⢉⡿⢯⣀⡇⠀⠀⠀⢿⠀⠀⠀⢸⡦⣤⣄⠀⠀⠀
⠀⢀⡴⠋⠀⠁⠹⣤⣀⡤⠏⠀⠀⠀⠐⣿⠹⣄⡼⠟⣿⣿⣿⣿⣿⣿⣿⣿⡶⠻⣶⡴⠿⡇⠀⠀⠀⠘⢦⣀⣠⠞⠃⠀⠈⠳⡀⠀
⢠⡟⠀⢠⡶⣄⠀⠀⢸⠀⠀⠀⠀⠀⠘⢿⣤⣼⣤⣤⣤⣶⣧⣶⣦⣶⣴⣦⣤⣤⣴⣤⣤⡇⠀⠀⠀⠀⠀⣼⠀⠀⣀⠶⣄⠀⠹⡄
⠸⣇⡴⠋⢠⠞⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⣨⡷⠀⢺⣆⢀⠀⠀⠀⢀⡽⠀⠀⠀⠀⠀⠀⠹⣄⠀⠹⣄⠈⢳⣠⠇
⠀⠙⠁⣴⣋⣀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠉⠉⠉⠉⠙⣦⡠⣶⠋⠉⠉⠉⠉⠉⢳⠄⠀⠀⠀⠀⠀⠀⠈⠣⣀⣙⣦⡀⠛⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⠖⠖⠲⠒⠒⠿⣇⡀⣨⠗⠒⠒⠒⠒⠲⣯⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣤⠤⠤⢴⢶⣶⡟⠂⢙⡦⠤⠤⢤⣤⣤⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠛⠚⠛⠚⠓⠲⢤⡷⠀⣻⠦⠖⠒⠛⠛⠛⠛⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⣺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣿⠁⢻⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''
print(Fore.RED+mask)
print("created by ©bobdaves-tech \n")
print("----------------------------------------------------")
import openai

openai.api_key = "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"

def chatGPT():
  prompt = input("\033[1;32m [mrROBOT]: Hello! How can I help you? (Type 'quit' to exit) \n" + "\n [YOU]: \n")
  while prompt != 'quit':
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=1094,
      temperature=0.5,
      n=1,
      stop=None
    )
    print("\033[1;32m \n [mrROBOT]:"+response['choices'][0]['text'])
    prompt = input("\n [YOU]: \n")

chatGPT()