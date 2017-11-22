import SaveFile

if __name__=='__main__':
    file=SaveFile.SaveFile('https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',"storage")
    file.save()