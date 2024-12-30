# Take website name as input # Check if the user wants to exit the program
# Open the website in the default web browser using call function
import webbrowser

def open_website():
    while True:
        
        website = input("Enter the website URL (type 'exit' to quit): ")
        
        
        if website.lower() == "exit":
            print("Exiting the program.")
            break
        
        else:
            webbrowser.open(f"www.{website}.com")


open_website()

