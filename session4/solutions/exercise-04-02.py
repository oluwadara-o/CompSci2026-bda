import multiprocessing as mp
import os
import shutil
import time
import urllib.request

from PIL import Image


image_urls = [
    "https://picsum.photos/id/10/300/200",
    "https://picsum.photos/id/20/300/200",
    "https://picsum.photos/id/30/300/200",
    "https://picsum.photos/id/40/300/200",
    "https://picsum.photos/id/50/300/200",
    "https://picsum.photos/id/60/300/200",
    "https://picsum.photos/id/70/300/200",
    "https://picsum.photos/id/80/300/200",
    "https://picsum.photos/id/90/300/200",
    "https://picsum.photos/id/100/300/200",
]


def download_and_rotate(item):
    index, url = item
    # item is a tuple: (index, url)
    # Download a free sample image
    urllib.request.urlretrieve(url, f"images/sample_{index}.jpg")

    # Open the image
    image = Image.open(f"images/sample_{index}.jpg")

    # Rotate it 90 degrees
    rotated_image = image.rotate(90, expand=True)

    # Save the new image
    rotated_image.save(f"processed/rotated_sample_{index}.jpg")



def serial_runner(urls):
    start = time.perf_counter()
    for index, url in enumerate(urls):
        print(f"Processing image {index} from {url}")
        download_and_rotate((index, url))
    end = time.perf_counter()
    print(f"Serial time: {end - start:.2f}s")


def pool_runner(urls, workers=4):
    start = time.perf_counter()
    # TODO
    ...
    tasks = [(index, url) for index, url in enumerate(urls)]

    with mp.Pool(processes=workers) as pool:
        results = pool.map(download_and_rotate, tasks)

    end = time.perf_counter()
    print(f"Pool time: {end - start:.2f}s")


if __name__ == "__main__":
    os.makedirs("images", exist_ok=True)
    os.makedirs("processed", exist_ok=True)

    serial_runner(image_urls)

    for folder in ["images", "processed"]:
        if os.path.exists(folder):
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)

    pool_runner(image_urls, workers=4)
