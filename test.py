from Image import Save
from Models.Complete.Image import Image
import os.path;
if __name__ == '__main__':
   # Image().file_path = 'storage/test.txt'
    img = Image()
    img.fetch()
    img.remove('https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwjh5vTS4tPXAhVMNI8KHXEWATYQPAgD')
    print(img.links)
    img.save()

    #print(os.path.basename('storage/complete/image.txt'))
    #print(os.path.dirname('storage/complete/image.txt'))