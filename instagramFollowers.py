from bs4 import BeautifulSoup
from urllib.request import urlopen

my_url = "https://www.instagram.com/cheerypal/"
page_open = urlopen(my_url)
soup_data = BeautifulSoup(page_open, "html.parser")
soup_text = soup_data.text
follow_index = soup_text.find("edge_followed_by")
fullname_index = soup_text.find("full_name")
fullname = soup_text[fullname_index + 12: fullname_index + 22]
fullname = fullname.split("}")[0]
followers = soup_text[follow_index + 27: follow_index + 37]
followers = followers.split("}")[0]

print(fullname + " has " + followers + " followers")
