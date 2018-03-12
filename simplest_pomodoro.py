import webbrowser
import random
import time

# Le Internet Medley, Nyan Cat, Caramelldansen, All Your Base Are Belong To Us, Tunak Tunak Tun, All Star
alarm_video_urls = ["https://www.youtube.com/watch?v=mghhLqu31cQ", "https://www.youtube.com/watch?v=QH2-TGUlwu4", "https://www.youtube.com/watch?v=EBOWWbCf-KU",
                    "https://www.youtube.com/watch?v=8fvTxv46ano", "https://www.youtube.com/watch?v=vTIIMJ9tUc8", "https://www.youtube.com/watch?v=L_jWHffIx5E",]

def tick_time(seconds):
    for s in range(1, seconds+1):
        time.sleep(1)
        print(s)

def main():
    tick_time(15)
    chosen_video = random.choice(alarm_video_urls)
    webbrowser.open(chosen_video)

if __name__ == '__main__':
    main()