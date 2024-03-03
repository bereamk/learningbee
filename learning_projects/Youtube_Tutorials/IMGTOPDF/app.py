import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from PIL import Image
import os

class ImageToPDFConverter:
    # Initialized our self and root
    def __init__(self, root):
        self.root = root # Root window
        self.image_paths = [] # List to store the paths of the selected images
        self.output_pdf_name = tk.StringVar() # StringVar to store the name of the output PDF
        self.selected_images_listbox = tk.Listbox(root, selectmode = tk.MULTIPLE) # Listbox to display the selected images

        self.initialize_ui() # Function to initialize the UI

    # Function to select images
    def initialize_ui(self): # Function to initialize the UI
        title_label = tk.Label(self.root, text = "Image to PDF Converter", font = ("Helvectica", 16, "bold"))
        title_label.pack(pady = 10) # Packing the title label

        # Select images button
        select_images_button = tk.Button(self.root, text = "Select Images", command = self.select_images)
        select_images_button.pack(pady = (0, 10))

        # Listbox to display selected images
        self.selected_images_listbox.pack(pady = (0, 10), fill = tk.BOTH, expand = True)

        # Convert button
        convert_button = tk.Button(self.root, text = "Convert to PDF", command = self.convert_images_to_pdf)
        convert_button.pack(pady = (20, 40))

    # Function to select images
    def select_images(self):
        self.image_paths = filedialog.askopenfilenames(title = "Select Images") # Opens a file dialog to select images, taking only pngs, jpgs, and jpegs
        self.update_selected_images_listbox() # Function to update the listbox with the selected images

    # Function to update the listbox with the selected images
    def update_selected_images_listbox(self):
        self.selected_images_listbox.delete(0, tk.END) # Checks if there is a previous selection and deletes it

        for image_path in self.image_paths: # Iterate through the selected images
            _, image_path = os.path.split(image_path) # Get the name of the image
            self.selected_images_listbox.insert(tk.END, image_path) # Insert the image name into the listbox
    
    # Function to convert the selected images to PDF
    def convert_images_to_pdf(self):
        try:
            if not self.image_paths:  # If no images are selected,
                return  
            
            # Let the user choose the output directory and file name
            output_pdf_path = asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if not output_pdf_path:  # If the user cancels the save dialog,
                return

            pdf = canvas.Canvas(output_pdf_path, pagesize = (612, 792)) # Create a PDF canvas with the specified size

            # Iterate through the selected images
            for image_path in self.image_paths:
                image = Image.open(image_path) # Open the image
                available_width = 540 # Width of the canvas
                available_height = 720 # Height of the canvas
                scale_factor = min(available_width / image.width, available_height / image.height) # Calculate the scale factor
                new_width = image.width * scale_factor # Calculate the new width
                new_height = image.height * scale_factor # Calculate the new height
                x_centered = (612 - new_width) / 2 # Calculate the x-coordinate to center the image
                y_centered = (792 - new_height) / 2 # Calculate the y-coordinate to center the image

                white = Color(255/255, 255/255, 255/255) # Set the fill color of the page to white
                pdf.setFillColor(white)
                pdf.drawInlineImage(image, x_centered, y_centered, width = new_width, height = new_height) # Draw the image on the canvas
                pdf.showPage() # Show the page

            pdf.save() # Save the PDF

            # Show a message box informing the user that the conversion is complete
            messagebox.showinfo("Success", "Images converted to PDF successfully!")

        except Exception as e:
            # Show a message box with the error message if an error occurs
            messagebox.showerror("Error", str(e))

# Function that defines the Window UI for the application
def main():
    root = tk.Tk() # Create a root window
    root.title("Image to PDF") # Set the title of the window
    converter = ImageToPDFConverter(root) # Create an instance of the ImageToPDFConverter class
    root.geometry("400x400") # Set the size of the window
    root.mainloop() # Run the application

if __name__ == "__main__": # If the script is run directly
    main() # Run the main function