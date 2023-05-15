from threading import Thread
import httpx


def oqim1():
    url = 'https://example.com'
    res = httpx.get(url)
    print(f"1-oqim {url} ga {res.status_code} so'rov jonatildi")


def oqim2():
    url = 'https://google.com'
    res = httpx.get(url)
    print(f"2-oqim {url} ga {res.status_code} so'rov jonatildi")


def oqim3():
    url = 'https://openai.com'
    res = httpx.get(url)
    print(f"3-oqim {url} ga {res.status_code} so'rov jonatildi")


def oqim4():
    url = 'https://stackoverflow.com'
    res = httpx.get(url)
    print(f"4-oqim {url} ga {res.status_code} so'rov jonatildi")


def oqim5():
    url = 'https://github.com'
    res = httpx.get(url)
    print(f"5-oqim {url} ga {res.status_code} so'rov jonatildi")


oqim_1 = Thread(target=oqim1)
oqim_2 = Thread(target=oqim2)
oqim_3 = Thread(target=oqim3)
oqim_4 = Thread(target=oqim4)
oqim_5 = Thread(target=oqim5)

#
oqim_1.start()
oqim_2.start()
oqim_3.start()
oqim_4.start()
oqim_5.start()

oqim_1.join()
oqim_2.join()
oqim_3.join()
oqim_4.join()
oqim_5.join()
