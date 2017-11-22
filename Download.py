import urllib.parse
import urllib.request
import os.path
import errno
import SaveFile


class Download():
    def __init__(self, file_name, path=''):
        self.links = set()
        self.completed = set()
        self.file_name = file_name
        self.file_to_set()
        self.path = path

    def file_to_set(self) -> object:
        """
        Load links from file and set to Set()
        :return: object
        """
        if not os.path.exists(self.file_name):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.file_name)
        with open(self.file_name, 'rt') as f:
            for line in f:
                self.links.add(line.replace('\n', ''))
        return sorted(self.links)

    def start(self) -> object:
        """
        Start Downloading file
        :rtype: object
        """
        for file in self.links:
            try:
                img = SaveFile.SaveFile(file, self.path)
                img.save()
            except:
                continue
            self.completed.add(file)
        self.set_to_file()

    def set_to_file(self) -> object:
        """
        Update links txt file
        :return : None
        """
        remaining = self.links.difference(self.completed)
        with open(self.file_name, 'w') as f:
            if len(remaining) > 0:
                for line in self.links:
                    f.write(line + "\n")
            f.write("")
