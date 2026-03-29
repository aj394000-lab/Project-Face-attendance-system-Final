#  Face Recognition-Based Attendance System

A real-time face recognition-based attendance system built using **Python**, **Django**, **OpenCV**, and **FaceNet-PyTorch**. This system captures student faces using a webcam, performs deep learning-based recognition, and marks attendance automatically in a contactless and secure manner.

---

## 📌 Key Features

- 🔐 Admin login with secure dashboard access
- 👨‍🎓 Student registration, authorization, and management
- 📸 Real-time facial recognition and attendance marking
- 📊 Detailed attendance reports and logs
- 🖥️ Bootstrap-powered responsive user interface
- 📂 SQLite backend for efficient data storage

---

## 🛠️ Technologies Used

| Technology      | Purpose                                |
|-----------------|----------------------------------------|
| Python 3.10+    | Core programming language              |
| Django          | Web framework                          |
| OpenCV          | Real-time video feed and image processing |
| FaceNet-PyTorch | Deep learning-based face recognition   |
| SQLite          | Lightweight database                   |
| Bootstrap       | Frontend design and responsiveness     |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/jhaakshat835-web/Project-Face-attendance-system-main.git
cd Project-Face-attandence-system
```
2. Create and Activate Virtual Environment
```bash
python -m venv venv
# For Windows
venv\Scripts\activate
```
3. Install Required Dependencies
```bash
pip install -r requirements.txt
```
4. Run the Django Server
```bash
python manage.py runserver
```
⚠️ Note for Windows Users: You must have Visual C++ Build Tools installed to compile some dependencies.
💡 Linux Users: No additional C++ setup is required.

## Run locally (Windows PowerShell)

If you use the included virtual environment, run the server from the inner project folder where `manage.py` lives.

PowerShell (activate then run):
```powershell
Set-Location "C:\Users\aj394\Downloads\Project-Face-attandence-system-main"
.\..\venv\Scripts\Activate.ps1
python manage.py runserver
```

Or run without activating the venv (direct call):
```powershell
& "C:\Users\aj394\Downloads\Project-Face-attandence-system-main\venv\Scripts\python.exe" "C:\Users\aj394\Downloads\Project-Face-attandence-system-main" python manage.py runserver
```

🔑 Admin Login Credentials

Username: TeamAKSH

Password: AKSH@123

Log in to the Django admin dashboard using the above credentials to manage student data, view attendance reports, and authorize students.
