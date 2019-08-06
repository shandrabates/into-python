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
    counter = 0
    while counter <3:
        # Delay/sleep for a few seconds"
        time.sleep(60*60)   # 1 hour
        webbrowser.open(video_address)
        counter += 1
        end = time.time()
        print(end - start)



if __name__ == '__main__':
    main()
    exit(0)
