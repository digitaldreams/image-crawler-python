import os.path
import urllib.parse
import errno


class Model:
    links = set()
    file_path = ''

    @classmethod
    def fetch(cls):
        """
            Load links from file and set to Set()
            :return: object
        """
        dir_name = os.path.dirname(cls.file_path)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            with open(cls.file_path, 'w') as f:
                f.write('')
        else:
            with open(cls.file_path, 'r') as f:
                for line in f:
                    cls.links.add(line.replace('\n', ''))
        return cls.links

    @classmethod
    def save(cls):
        """

        :type links: object
        """
        with open(cls.file_path, 'w') as f:
            for line in sorted(cls.links):
                f.write(line + "\n")
        return True

    @classmethod
    def has(cls, link):
        if not link in cls.links:
            return False
        else:
            return True

    @classmethod
    def add(cls, link):
        cls.links.add(link)
        return cls

    @classmethod
    def remove(cls, link):
        cls.links.remove(link)
        return cls
