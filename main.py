import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename
import threading

# Function for text-to-speech
def speak_text(text):
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()

# Open file dialog to select a PDF file
book = askopenfilename()

try:
    # Open the selected PDF file
    with open(book, "rb") as file:
        pdfreader = PyPDF2.PdfReader(file)
        pages = len(pdfreader.pages)

        for num in range(pages):
            page = pdfreader.pages[num]
            text = page.extract_text()

            if text:
                # Use threading to run the speak_text function without blocking
                speech_thread = threading.Thread(target=speak_text, args=(text,))
                speech_thread.start()
                speech_thread.join()  # Wait for the speech thread to finish before continuing

        print("\nFinished reading the PDF.")

except KeyboardInterrupt:
    print("\nProgram interrupted. Exiting smoothly.")

except Exception as e:
    print(f"\nAn error occurred: {e}")

finally:
    print("Cleaning up resources... Done!")
