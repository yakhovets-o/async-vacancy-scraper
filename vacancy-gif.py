import os
from PIL import Image

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
gif_path = os.getenv('gif_path')


def create_gif() -> None:
    frames = []
    for file in os.listdir(path=gif_path):
        frame = Image.open(gif_path + file)
        frames.append(frame)

    frames[0].save(
        'vacancy.gif',
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=100,
        loop=0
    )
