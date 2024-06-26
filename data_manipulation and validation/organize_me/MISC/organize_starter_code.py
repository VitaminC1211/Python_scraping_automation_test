import os
from pathlib import Path

SUBDIRECOTRIES = {
    "DOCUMENTS": ['.pdf', '.rtf','.txt'],
    "AUDIOUS": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png']
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECOTRIES.items():
        if value in suffixes:
            return category
    return "MISC"

# test out the pickDirectory() function
print(pickDirectory(".pdf"))

def organizeDirecotry():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDirectory(fileType)
        directoryPath = Path(directory) 
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

# test out the organizeDirectory() function
organizeDirecotry()



        