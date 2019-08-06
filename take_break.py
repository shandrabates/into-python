""""
Set an alarm to take a break by playing a youtube video
"""

import webbrowser

video_address = "https://www.youtube.com/watch?v=_tcW-j7KFgY"

import time

start = time.time()
print("hello")


def main():
    """
    Open a youtube link to a song I like
    :return: nothing
    """
    video_address = "https://www.youtube.com/watch?v=_tcW-j7KFgY"
    webbrowser.open(video_address)
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()
    exit(0)
