'''
python code for converting images to video where images are stored in a folder 
named in serial order like 0.jpg, 2.jpg .... 99.jpg
video should be stored in the same folder where images are stored

'''
import cv2
import os
import numpy as np
from os.path import isfile, join
import pdb
def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
 
    #for sorting the file names properly
    # files.sort(key = lambda x: int(x[5:-4]))
    files.sort(key = lambda x: int(x.split('.')[0]))

 
    for i in range(len(files)):
        if i == 100:
            break
        # pdb.set_trace()
        filename=os.path.join(pathIn, files[i])
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
        #inserting the frames into an image array
        frame_array.append(img)
 
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()

def main():
    pathIn= r'C:\Users\UMA\Desktop\fall2024\image_synth\final_project_presentation\results\clemson\stroke'
    pathOut = os.path.join(pathIn, 'video.avi')
    fps = 24.0
    convert_frames_to_video(pathIn, pathOut, fps)

if __name__=="__main__":
    main()