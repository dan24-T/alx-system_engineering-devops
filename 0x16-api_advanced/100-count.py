#!/usr/bin/python3
""" We query the Reddit API recursively with the function created count words """



def count_words(subreddit, word_list, after='', word_dict={}):
    """ Well weve created our function now th fun begins.
    """
    import requests

    if not word_dict:
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0

    if after is None:
        wordict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word in wordict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

    B_url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'redquery'}
    p = {'limit': 100, 'after': after}
    response = requests.get(B_url, headers=header, params=p,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        hot = response.json()['data']['children']
        aft = response.json()['data']['after']
        for post in hot:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in word_dict.keys():
                word_dict[word] += lower.count(word)

    except Exception:
        return None

    count_words(subreddit, word_list, aft, word_dict)