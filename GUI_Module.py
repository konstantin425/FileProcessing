from Tkinter import *
import tkFileDialog
from os import path
import csv
from datetime import datetime



class CsvGuiClass(Frame):

    # opens file selection window. Calls OpeanAndRead
    def fileSelect(self):
        self.filename = tkFileDialog.askopenfilename(filetypes=[("CSV","*.csv")])

        # instantiate a FileOps object in order to use the OpenAndRead method
        selectObj = FileOps()
        selectObj.openAndRead(self.filename, 10,5)


    def createWidgets(self):

        # Creating frames which are "containers" to hold widgets and buttons in the window
        # Create 2 frames - top and bottom
        self.topFrame = Frame(root)
        self.topFrame.pack()
        self.bottomFrame = Frame(root)
        self.bottomFrame.pack(side=BOTTOM)

        # First widget - date and time on the top frame
        today = datetime.now()
        topLabel = Label(self.topFrame, text=today, fg="blue")
        topLabel.pack()

        # Create buttons on the bottom frame
        # Button 1: file selection
        self.button1 = Button(self.bottomFrame, text="Select the .cvs file",command=self.fileSelect)
        self.button1.pack(side=LEFT)
        # Button 2: Exit
        self.button2 = Button(self.bottomFrame, text="Exit!", command=self.bottomFrame.quit)
        self.button2.pack(side=RIGHT)

    # initialization function runs upon the instantiation of this object
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.filename = None
        self.pack()
        self.createWidgets()


class FileOps():

    # Accepts 1) path-file object, 2)the number of rows 3) number of columns.
    # Performs error checking against .csv extension
    # Reads the csv file row by row. Prints out results in a "matrix" form. No return
    def openAndRead(self, file, rows, col):
        # Error checking. Report an error if not a csv file
        fileExtention = str(path.basename(file))
        if (fileExtention[-3:] != "csv"):
            print "\n Pick a CSV file! \n"

        else:
            with open(file, "r") as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                k = 0;
                for row in reader:
                    while (k < rows):
                        print (row[0:col])
                        k = k + 1



# **********************************************************************************************************************
#                                                 Begin main
# **********************************************************************************************************************

def main():

    # start main GUI window. Instantiate a CsvGuiClass object
    global root
    root = Tk()
    root.title("Main window")
    mainWindow = CsvGuiClass(master=root)
    mainWindow.mainloop()




if __name__ == "__main__":
    main();

# **********************************************************************************************************************
#                                                 end main
# **********************************************************************************************************************