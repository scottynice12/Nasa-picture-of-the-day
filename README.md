# NASA Picture API – Flask

1.A simple web API that serves NASA's Astronomy Picture of the Day (APOD).  
Two endpoints:  
- `/apod` → JSON with title and image URL  
- `/apod/image` → the actual image

Anyone can run it on their own computer – or deploy it for a live URL.

---

## 🚀 Run it yourself (5 minutes)

### 1. Open a terminal
- **Windows**: Press `Win + R`, type `cmd`, press Enter  
- **Mac**: `Cmd + Space`, type `Terminal`  
- **Linux**: `Ctrl + Alt + T`

### 2. Get the code
From the file I got in here
**Option A – Download `app.py` directly**  
Save the code from the bottom of this README as `app.py` inside a new folder (e.g., `nasa_api_project`).

**Option B – Clone the repo**  
```bash
git clone https://github.com/yourusername/nasa-picture-api.git
cd nasa-picture-api

Step 3:Install Flask and requests
pip install flask requests
(If pip not found, use python -m pip install flask requests.)

Step 4:Run the server
python app.py

You'll see:
* Running on http://randomnumbers
You put /apod or /apod/image at the end of the URL cuz they are endpoints

5. Open your browser and visit:
Get JSON → http://randomnumbers/apod
Get image → http://randomnumbers/apod/image
That's it – your own NASA API is running locally.

🆘 Help! I can’t find my folder in the terminal
If you saved app.py on your Desktop or Documents, but the terminal says “no such file”:

6.Windows
In File Explorer, go to the folder containing app.py.
Click the address bar – copy the full path (e.g., C:\Users\YourName\OneDrive\Desktop\nasa_api_project).
In Command Prompt, type: (Click windows R)
cmd
cd "C:\Users\YourName\OneDrive\Desktop\nasa_api_project"
(Use double quotes if the path has spaces.)
Then run python app.py again.

6b.Mac / Linux
Open Terminal.
Type cd (with a space) – do not press Enter yet.
Drag the folder from Finder into the Terminal window – the path appears automatically.
Press Enter.
Run ls to see if app.py is there, then python app.py.

MAKE sure you copy my code in the app.py file before you go and try to run it

Get a live URL (for anyone, anywhere)
Right now your API only works on your computer (random numbers).
To get a real URL like https://your-name.pythonanywhere.com/apod, deploy it for free:

7.Deploy on PythonAnywhere (10 minutes)
Create a free account at pythonanywhere.com.
Go to Files → upload your app.py.
Go to Web → add a new web app → choose Flask.
Set the source file to /home/yourusername/mysite/app.py.
Click Reload.
Your live endpoints become:
https://yourusername.pythonanywhere.com/apod
https://yourusername.pythonanywhere.com/apod/image
Now you can put those links in your portfolio or share them with anyone.

8.Example response (JSON)
When you visit /apod (locally or live), you'll see:
json
{
  "title": "Comet R3 PanSTARRS and Orion",
  "url": "https://apod.nasa.gov/apod/image/2605/CometOrion_Perrot_960_annotated.jpg"
}
Use the /apod/image endpoint to get the actual picture directly.

9. Stop the server
Press Ctrl + C in the terminal where the server is running.

📄 License
MIT – free to use, modify, and share.
text

---

Now your README has **everything**:
- Terminal navigation help (even for beginners)
- Local run instructions with `127.0.0.1` endpoints
- Deployment guide for a real `https://something.com/apod` URL
- Both endpoints documented
You can paste this directly into your GitHub repo. Want me to also write a short `deployment-guide.md` for PythonAnywhere with screenshots?




