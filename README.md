# Anime Episode Preview Downloader
Download images of anime's episode previews from official and news websites

## Introduction
Anime Episode Preview Downloader downloads images of previews of episodes from official websites. The program is written in Python 3. The program uses multiprocessing to download the images quickly.

## Setting Up
1. Download and install the latest version of [Python](https://www.python.org/downloads/)
2. Open the Command Prompt (for Windows) or Terminal (for MacOS).
3. Run the following commands:
```
pip install requests
```

## Running the Program
1. Using the Command Prompt (Terminal for MacOS), change to the directory to where the file `run.py` is located.
2. Open `run.py` with a plain text editor (e.g. Notepad) and uncomment (remove the first '#') all the anime you want to download (see picture):
![image001.png](/images/example.png)
3. Once you uncomment all the anime you wanted to download, save it.
4. Going back to the Command Prompt (or Terminal), run the following command: `python run.py`
5. The images will be saved at the folder `download`.
