import cv2
import numpy as np
import glob
from os.path import isfile, join
import subprocess
from IPython.display import clear_output  

#convert super res frames to .avi  
      pathIn = ' /content/GPEN/examples/out-gpen/'

      zee = zee+1
      fName = "video"+str(zee)  
      filenameVid = f"{fName}.avi"
        
      pathOut = "/content/GFPGAN/results_videos/"+filenameVid

      fps = 25.0 #change this to FPS of your source video

      convert_frames_to_video(pathIn, pathOut, fps)      

      #after processing frames converted to .avi video , delete upscaled frames from previous video
      for f in os.listdir('results/restored_imgs'): 
          os.remove(os.path.join('results/restored_imgs', f))

      #convert .avi to .mp4
      src = '/content/GFPGAN/results_videos/'
      dst = '/content/GFPGAN/results_mp4_videos/'

      for root, dirs, filenames in os.walk(src, topdown=False):
          #print(filenames)
          for filename in filenames:
              print('[INFO] 1',filename)
              try:
                  _format = ''
                  if ".flv" in filename.lower():
                      _format=".flv"
                  if ".mp4" in filename.lower():
                      _format=".mp4"
                  if ".avi" in filename.lower():
                      _format=".avi"
                  if ".mov" in filename.lower():
                      _format=".mov"

                  inputfile = os.path.join(root, filename)
                  print('[INFO] 1',inputfile)
                  outputfile = os.path.join(dst, filename.lower().replace(_format, ".mp4"))
                  subprocess.call(['ffmpeg', '-i', inputfile, outputfile])  
              except:
                  print("An exception occurred")        
  
      clear_output(wait=True)

      #clearing previous .avi files
      for f in os.listdir(video_result_folder): 
          os.remove(os.path.join(video_result_folder, f))

      #deletes frames from previous video
      #for f in os.listdir(upload_folder):
      #  os.remove(os.path.join(upload_folder, f))

        

      # if it is out of memory, try to use the `--tile` option
# We upsample the image with the scale factor X3.5

# Arguments
# -n, --model_name: Model names
# -i, --input: input folder or image
# --outscale: Output scale, can be arbitrary scale factore. 