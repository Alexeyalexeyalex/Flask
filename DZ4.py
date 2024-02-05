import threading
import time
import requests
import multiprocessing
import aiohttp
import asyncio
import sys

urls = [
'https://wp-s.ru/wallpapers/14/5/370113389335123/abstrakciya-s-izobrazheniem-devushki-s-zel-nymi-gubami.jpg',
'https://n1s1.hsmedia.ru/5c/a9/92/5ca9922dcd2f2a2304a3851c058f020f/1585x951_0xac120003_9986014371588926575.jpg',
'https://img.razrisyika.ru/kart/82/324687-igry-na-pk-2.jpg',
'https://gas-kvas.com/uploads/posts/2023-02/1675497297_gas-kvas-com-p-fonovie-risunki-dlya-rabochego-stola-na-ve-50.jpg',
'https://w.forfun.com/fetch/30/3048bfefbbcf5efb84c57cd07698afeb.jpeg',
'https://static.onlinetrade.ru/img/fullreviews/38380/6_big.jpg',
'https://w.forfun.com/fetch/76/7634042337199e726ab1936bd62a2911.jpeg',
'https://w-dog.ru/wallpapers/1/55/338390184920084/assassins-creed-oruzhie-ubisoft-ogon-voin.jpg'
]


threads = [] 
mult = []

start_time = time.time()


def download(_url):
    response = requests.get(_url)
    name = _url.split("/")
    out = open(f".\{name[-1]}", "wb")
    out.write(response.content)
    out.close()
    print(f"Downloaded {_url} in {time.time() - start_time:2f} seconds")

async def async_download(my_urls):
    response = requests.get(my_urls)
    name = my_urls.split("/")
    out = open(f".\{name[-1]}", "wb")
    out.write(response.content)
    out.close()
    print(f"Downloaded {my_urls} in {time.time() - start_time:2f} seconds")
    await asyncio.sleep(1)


# многопоточный
def multithreaded(my_urls = urls):
    if __name__ == '__main__':
        for url in urls:
            thread = threading.Thread(target=download, args=[url])
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()   

# многопроцессорный 
def multiprocessor(my_urls=urls):

    for url in my_urls:
        thread = multiprocessing.Process(target=download, args=[url])
        mult.append(thread)
        thread.start()

    for thread in mult:
        thread.join()
        print(f"Downloaded in {time.time() - start_time:2f} seconds")

    
# асинхронный 
async def main(my_urls = urls):
    task = []
    for url in my_urls:
        task.append(asyncio.create_task(async_download(url)))
        await asyncio.gather(*task)

    
if __name__ == '__main__':

    # if len(sys.argv) > 1:
    #     multiprocessor(sys.argv[1:])
    #     multithreaded(sys.argv[1:])
    # else:
    #     multiprocessor()
    #     multithreaded()

    asyncio.run(main())
    print(f"Downloaded in {time.time() - start_time:2f} seconds")