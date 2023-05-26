import cv2
import os
import tkinter as tk
from tkinter import filedialog

class VideoToImagesApp:
    def __init__(self, master):
        self.master = master
        master.title("Video to Images Converter")

        self.numb_label = tk.Label(master, text="Number of scrinshots of the video file:")
        self.numb_label.pack()

        self.numb_entry = tk.Entry(master)
        self.numb_entry.pack()

        self.path_label = tk.Label(master, text="Path to the video file:")
        self.path_label.pack()

        self.path_entry = tk.Entry(master)
        self.path_entry.pack()

        self.name_entry = self.path_entry.get()[self.path_entry.get().rfind("\\")+1:]

        self.path_button = tk.Button(master, text="Browse", command=self.browse_path)
        self.path_button.pack()

        self.new_path_label = tk.Label(master, text="Path to save the images:")
        self.new_path_label.pack()

        self.new_path_entry = tk.Entry(master)
        self.new_path_entry.pack()

        self.new_path_button = tk.Button(master, text="Browse", command=self.browse_new_path)
        self.new_path_button.pack()

        self.run_button = tk.Button(master, text="Run", command=self.run)
        self.run_button.pack()

    def browse_path(self):
        path = filedialog.askopenfilename()
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0, path)

    def browse_new_path(self):
        new_path = filedialog.askdirectory()
        self.new_path_entry.delete(0, tk.END)
        self.new_path_entry.insert(0, new_path)

    def run(self):
        name = self.name_entry
        path = self.path_entry.get()
        new_path = self.new_path_entry.get()
        numb = int(self.numb_entry.get())
        cap = cv2.VideoCapture(path)

        fps = cap.get(cv2.CAP_PROP_FPS)
        print(fps)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(frame_count)

        for i in range(1, numb+1):
            frame_number = int(i / numb * frame_count // 1 - 1)
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            # Read the next frame from the video
            ret, frame = cap.read()
            print(ret)
            # Save the frame as an image file
            print(cv2.imwrite(new_path +'/'+name.replace('.mp4','')+f"{i}.jpg", frame))
            print(os.listdir(new_path))

        # Release the video file and exit the program
        cap.release()
        cv2.destroyAllWindows()

root = tk.Tk()
app = VideoToImagesApp(root)
root.mainloop()
