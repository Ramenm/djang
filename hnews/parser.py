import bs4
from urllib.request import urlopen
from hnews.models import Post
from functools import wraps
import time

def loop_decorator(time_to_sleep):
    def func_wrap(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            while True:
                func(*args, **kwargs)
                time.sleep(time_to_sleep)
        return wrapper
    return func_wrap

@loop_decorator(time_to_sleep=2*60)
def post_parse_and_create():
    c = urlopen('https://news.ycombinator.com').read()

    bs = bs4.BeautifulSoup(c, 'lxml')
    tr_elements = bs.find_all('a', {'class': 'storylink'})

    posts_list = [Post(title=i.text, url=i.get('href')) for i in tr_elements]


    to_add = set(i.title for i in posts_list)
    exist = set(i.title for i in Post.objects.order_by('-pk')[0:90])
    add_set = to_add - exist
    print(add_set)
    print(len(add_set))

    posts_dict = dict((i.title, i) for i in posts_list)
    Post.objects.bulk_create([posts_dict[i] for i in add_set])

if __name__ == '__main__':
    post_parse_and_create()