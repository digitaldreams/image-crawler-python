import urllib.request
import urllib.parse
from functions import *
import ImgFinder
import Download

if __name__ == '__main__':
    PAGE_URL = 'https://gopostie.com/how-it-works'
    # Create the project folder into storage folder
    create_project_folder(PAGE_URL)
    # Find images source and save it to project folder
    finder = ImgFinder.ImgFinder(PAGE_URL)
    finder.feed(html_string(PAGE_URL))
    file_name = finder.save_to_file()
    #start downloading images
    down = Download.Download(file_name, finder.folder_path())
    down.start()
