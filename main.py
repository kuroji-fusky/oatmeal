from typing import Optional
import argparse
from pytube import YouTube
import ffmpeg
import os

class Oatmeal:
    def __init__(self, local_file: str, yt_link: Optional[str] = "") -> None:
        """
        Oatmeal class to oatmeal-ify your video saved on your system or via a YouTube
        video of your choice, note that longer videos will take a while depending
        on your computer's resources

        :param yt_link: Any YouTube link
        :param local_file: Local file that contains a supported video codec.
        """
        if local_file:
            """
            check if the file is from a supported video codec, otherwise, throw error
            if txt file
                - iterate and look for any supported video codec, throw error otherwise
                - if file not found, warn user, then proceed to video processing
            """

        if yt_link:
            if yt_link.lower().endswith('.txt'):
                print("do stuff")

    def mix(self, quality: int):
        """
        Turns the input then mix and beats it up till it turns into an oatmeal hah

        :param quality: Set quality scale from 1 to 10 (even setting 10 is still shit lmao)
        :return: Your final product lol
        """
        pass


def main():
    oatmeal = Oatmeal

    parser = argparse.ArgumentParser(description='Oatmeals your video for a funny low-quality memes')

    parser.add_argument('-i', '--input', required=True, description="Input for a local file, or a YouTube link")
    parser.add_argument('-o', '--output', description="Output file, default to the current directory")
    parser.add_argument('-q', '--quality', description="Quality of your oatmeal")

    args = parser.parse_args()

if __name__ == '__main__':
    main()
