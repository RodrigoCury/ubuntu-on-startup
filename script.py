import os
import webbrowser
import time

PATH_TO_OPEN = 'PATH/TO/FOLDER'


def open_all_files_in_directory(path):
    for filename in os.listdir(path):
        if filename == "websites.txt":
            open_all_websites(filename)
        if filename == "ubuntu-apps.txt":
            open_all_ubuntu_apps(filename)
    os.system("exit")


def open_all_websites(filename):
    with open(os.path.join(PATH_TO_OPEN, filename)) as file:
        for website in file.readlines():
            time.sleep(5)
            webbrowser.open(website, new=0, autoraise=False)


def open_all_ubuntu_apps(filename):
    with open(os.path.join(PATH_TO_OPEN, filename)) as file:
        for app in file.readlines():
            os.system(app)


if __name__ == "__main__":
    open_all_files_in_directory(PATH_TO_OPEN)
