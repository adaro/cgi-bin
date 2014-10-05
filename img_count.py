#No shebang line, please run in Linux shell % python img_count.py

#Python libs
import threading, urllib2, re
import Queue, json, time, pprint

#Global lists
JSON_LIST = list()
URLS = list()

def get_movies():
    url = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?apikey=[APIKEY]"
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    return data


def get_imgs(html):
    total = 0
    # This next line is not ideal. Would much rather use a lib such as Beautiful Soup for this
    total += len(re.findall(r"<img[^>]*>", html))
    return total


def read_url(url, queue):
    data = urllib2.urlopen(url).read()
    queue.put(data)


def fetch_urls():
    result = Queue.Queue()
    threads = [threading.Thread(target=read_url, args = (url,result)) for url in URLS]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return result


if __name__ == "__main__":
    start = time.time()
    movies = get_movies()
    for movie in movies["movies"]:
        url = "http://www.imdb.com/title/tt" + movie['alternate_ids']['imdb']
        URLS.append(url)
    queue = fetch_urls()
    while movies["movies"]:
        movie = movies["movies"].pop()
        job = queue.get()
        total = get_imgs(job)
        json_dict = {
                "title": movie['title'],
                "url": "http://www.imdb.com/title/tt" + movie['alternate_ids']['imdb'],
                "imdb_id": movie['alternate_ids']['imdb'],
                "count": total
                }
        JSON_LIST.append(json_dict)
    pprint.pprint(JSON_LIST)
    end = time.time()
    print "\n"
    print "Elapsed Time (seconds):", end - start
