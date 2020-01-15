#!/usr/local/bin/python
from dataclasses import dataclass
from typing import List
import os
import sys

@dataclass
class Photo:
    position: str
    tagsCount: int
    tags: List[str]
    
    def AddTag(self,tag):
        self.tags.append(tag)
        

class Slide: 
    def __init__(self,slide):
        self.slide = slide
    
    def CheckPosition(self):
        pass


def AverageTagsPerPhoto(photosList):    
    return allTagsCount/len(photosList)


photosList = []
allTagsCount = 0

pathToFile = os.getcwd() + "/QualificationRound2019.in/" + sys.argv[1]

with open(pathToFile) as fileObject:
    photosCount = int(fileObject.readline())
    #print(photosCount)
    for i in range(photosCount):
        photo = fileObject.readline().rstrip().split(' ')
        
        tagsCount = int(len(photo[2:]))
        position = photo[0]
        
        photosList.append(Photo(position,tagsCount,[]))
        allTagsCount += tagsCount
       # print(f'Tags count: {tagsCount}')
        for j in range(tagsCount):
            tag = photo[j+2].rstrip()
            #print(f'Tag: {tag}', end= " ")
            photosList[i].AddTag(tag)

#for x in photosList:
   #print(f'Tags count: {x.tagsCount}')
   #print(f'Tags list: {x.tags}')

print(f'Photos count: {len(photosList)}')
print(f'Average tags per photo: {AverageTagsPerPhoto(photosList)}')
print(f'All tags: {allTagsCount}')
