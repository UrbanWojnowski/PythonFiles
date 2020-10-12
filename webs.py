import requests
import bs4

#sending request with URL
URL='http://www.wp.pl'

response = requests.get(URL)
# print(response.text)
# print(response.status_code)

# f = open("result.txt",'wb')
#
# for data in response.iter_content(10000):
#     f.write(data)
#
# f.close()

# BS4 fetching data

parsed_data = bs4.BeautifulSoup(response.text)

all_links = parsed_data.select('a')

for l in all_links:
    print(l.get('href'))
    print(l.get('title'))
    #print(l.getText())
