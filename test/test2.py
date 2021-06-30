import multiprocessing
import time


def witsclient():
    while True:
        print("I am getting data from WITS server")
        time.sleep(1)

def mqttclient():
    while True:
        print("I am getting from the wits client")
        time.sleep(1)


if __name__ == '__main__':

    p1 = multiprocessing.Process(target=witsclient)
    p2 = multiprocessing.Process(target=mqttclient)

    p1.start()
    p2.start()

    p1.join()
    p2.join()