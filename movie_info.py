import sys
import requests
from bs4 import BeautifulSoup
movie_name = str(sys.argv[1])
rating = []
search_url = ('https://www.imdb.com/find?q=' +
              movie_name + '&s=tt&ref_=fn_al_tt_mr')
search_response = requests.get(search_url)
search_filter = BeautifulSoup(search_response.content, 'html.parser')
movies = search_filter.find_all("td", {"class": "result_text"})
for tag in movies:
    print ('\n')
    print ('Name : ' + tag.contents[1].text)
    movie_tag = tag.contents[1]['href']
    rating_url = 'https://www.imdb.com' + movie_tag + '?ref_=fn_tt_tt_1'
    rating_response = requests.get(rating_url)
    rating_filter = BeautifulSoup(rating_response.content, 'html.parser')
    ratings = rating_filter.find('span', {'itemprop': 'ratingValue'})
    if ratings is None:
        print('Currently No Ratings')
    else:
        print(ratings.text + ' Out of 10')
        rating.append(float(ratings.text))
average_rating = sum(rating) / len(rating)
print ('Average Rating is ', average_rating)
