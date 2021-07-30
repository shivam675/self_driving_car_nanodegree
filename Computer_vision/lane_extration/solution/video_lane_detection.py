import cv2
import numpy as np


video_file = 'challenge.mp4'
cap = cv2.VideoCapture(video_file)
if (cap.isOpened()== False):
    print("Error opening video stream or file")
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    # Display the resulting frame
    
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    kernel_size = 3
    blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)

    low_threshold = 100
    high_threshold = 255
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)



    rho = 2
    import numpy as np
    theta = np.pi/180
    threshold = 5
    min_line_length = 40
    max_line_gap = 10
    line_image = np.copy(edges)*0 #creating a blank to draw lines on
    # Press Q on keyboard to  exit
    lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                            min_line_length, max_line_gap)

    for line in lines:
        for x1, y1, x2 ,y2 in line:
            cv2.line(line_image, (x1,y1),(x2,y2),(255,255,0),3)

    # color_edges = np.dstack((edges, edges, edges))
    combo = cv2.addWeighted(edges, 0.8, line_image, 1, 0) 
    cv2.imshow('Frame',combo)

    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  # Break the loop
  else: 
    break

# When everything done, release the video capture object
cap.release()
# Closes all the frames
cv2.destroyAllWindows()