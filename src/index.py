import cv2
import sys

upper_left = (560, 20)
bottom_right = (200, 234)

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

source = cv2.VideoCapture(s)

win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

frame_width = int(source.get(3))
frame_height = int(source.get(4))
   
size = (frame_width, frame_height)
   
# Below VideoWriter object will create
# a frame of above defined The output 
# is stored in 'filename.avi' file.
result = cv2.VideoWriter('filename.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)

while cv2.waitKey(30) != 27: #Escape
    has_frame, frame = source.read()
    if not has_frame:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    r = cv2.rectangle(gray_frame, upper_left, bottom_right, (100, 50, 200), 5)
    rect_img = gray_frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]]

    sketcher_rect = rect_img

    gray_frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]] = sketcher_rect

    cv2.imshow(win_name, gray_frame)

source.release()
cv2.destroyWindow(win_name)