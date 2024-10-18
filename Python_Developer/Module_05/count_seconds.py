import time
def count_seconds(seconds):
    for i in range(1, seconds+1):
        print(i, end=' ')
        time.sleep(1)

if __name__ == '__main__':
    count_seconds(15)