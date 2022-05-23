from tkinter import *
import random
import os
from PIL import Image
from PIL import ImageTk
from moviepy.editor import *



root = Tk()
root.title("WOW SO COOL")


# varibles that help within the functions
y = 0
i = 0
x = 0



def PopPhoto():
    # function that shows on the grid a random photo from a file

    global x
    global random_image
    global open_random_img
    global label_photo
    global photo_path_list
    global resized_image

    # cheking if there is already an image, and if there is, removing it.
    try:
        if label_photo.winfo_exists():
            label_photo.grid_remove()
    except:
        pass

    # creating a list of photo paths from the wanted file
    photo_path_list = []
    path = r"/Users/marygrankin/Documents/Big_Trip_photos/"
    files = os.listdir(path)

    # making sure it is an image file and adding the path to the list of paths.
    for photo in sorted(files):
        if photo.endswith(('.jpg', '.png', 'jpeg')):
            img_path = path + photo
            photo_path_list.append(img_path)

    # choosing a random image from the list to open
    random_image = random.choice(photo_path_list)
    open_random_img = Image.open(random_image)

    # resizing the images to fit the grid and cheking if they are horizontal or vertical.
    width, height = open_random_img.size
    if width > height:
        resized_image = open_random_img.resize((600, 410), Image.Resampling.LANCZOS)
    
    else:
        resized_image = open_random_img.resize((410, 600), Image.Resampling.LANCZOS)

    # making the photo a label and adding it on the grid
    new_image = ImageTk.PhotoImage(resized_image)
    label_photo = Label(root, image = new_image)
    label_photo.image = new_image
    label_photo.grid(row = 5, column = 2)

    # setting the rotation count
    x = 0


def PopVideo():
    # function that opens a random video from a file 

    video_path_list = []
    path = "/Users/marygrankin/Documents/Big_Trip_Photos/"
    files = os.listdir(path)
    for video in files:
    # make sure file is a video
        if video.endswith(('.mov', '.mp4')):
            vid_path = path + video
            video_path_list.append(vid_path)

    random_num = random.randint(0, len(video_path_list) + 1)


    clip = VideoFileClip(video_path_list[random_num])

    clip.preview(fps = 20)



def forwards():
    # functions that forwards to the next photo in order 

    global x
    global y
    global i
    global random_image
    global open_random_img
    global label_photo
    global photo_path_list
    global resized_image

    # keeping count to forward to the next photo
    i += 1

    # removing the former photo
    label_photo.grid_forget()

    # checking the photo index
    photo_index = photo_path_list.index(random_image)

    # checking the photo index is still in the list, if not it starts from the first photo
    try:
        open_random_img = Image.open(photo_path_list[photo_index + i])
        
    except:
        open_random_img = Image.open(photo_path_list[y])
        y += 1

    # resizing the images to fit the grid and cheking if they are horizontal or vertical.
    width, height = open_random_img.size
    if width > height:
        resized_image = open_random_img.resize((600, 410), Image.Resampling.LANCZOS)

    else:
        resized_image = open_random_img.resize((410, 600), Image.Resampling.LANCZOS)

    # making the photo a label and adding it on the grid
    new_image = ImageTk.PhotoImage(resized_image)
    label_photo = Label(root, image = new_image)
    label_photo.image = new_image
    label_photo.grid(row = 5, column = 2)

    # setting the rotation count
    x = 0
    

    

def backwards():
    # functions that backwards to the preview photo in order 

    global x
    global i
    global random_image
    global open_random_img
    global label_photo
    global photo_path_list
    global rotated_label
    global resized_image

    # keeping count to backwards to the preview photo
    i -= 1
    
    # removing the former photo
    label_photo.grid_remove()

    # checking the photo index and opening the photo
    photo_index = photo_path_list.index(random_image)
    open_random_img = Image.open(photo_path_list[photo_index + i])

    # resizing the images to fit the grid and cheking if they are horizontal or vertical.
    width, height = open_random_img.size
    if width > height:
        resized_image = open_random_img.resize((600, 410), Image.Resampling.LANCZOS)

    else:
        resized_image = open_random_img.resize((410, 600), Image.Resampling.LANCZOS)
        
    # making the photo a label and adding it on the grid
    new_image = ImageTk.PhotoImage(resized_image)
    label_photo = Label(root, image = new_image)
    label_photo.image = new_image
    label_photo.grid(row = 5, column = 2)

    # setting the rotation count
    x = 0


def rotate():
    # function that rotates the photo

    global x
    global random_image
    global label_photo
    global open_random_img
    global resized_image
    global rotated_label

    # removing the former photo
    label_photo.grid_forget()

    # keeping the rotation count to keep rotating 
    x += 1
    
    # rotating the image
    rotated_img = resized_image.rotate(270 * x)

    # making the photo a label and adding it on the grid
    new_image = ImageTk.PhotoImage(rotated_img)
    rotated_label = Label(root, image = new_image)
    rotated_label.image = new_image
    rotated_label.grid(row = 5, column = 2)

    # making the rotated label the same label as the rest to be able to remove it with the next function
    label_photo = rotated_label



#making the labels and the buttons

txt_label = Label(root, text = 'Do you want to see photos or videos from my trip?')
answer_1 = Button(root, text = 'A random photo please!', command = PopPhoto)
answer_2 = Button(root, text = 'A random video please!', command = PopVideo)
button_forwards = Button(root, text = '<<', command = backwards) 
button_backwards = Button(root, text = '>>', command = forwards) 
rotate_button = Button(root, text = 'rotate photo', command = rotate)


# adding the labels and bottons on the grid 

txt_label.grid(row = 1, column = 2, pady = 10)
answer_1.grid(row = 3, column = 2)
answer_2.grid(row = 4, column = 2)
button_forwards.grid(row = 5, column = 1)
button_backwards.grid(row = 5, column = 3, pady = 10)
rotate_button.grid(row = 6, column = 2)



root.mainloop()

