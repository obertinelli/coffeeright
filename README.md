# Coffeeright Ordering System

A web application for browsing the menu and placing pickup orders for Coffeeright, a local coffee shop.  
Built using Python, Django, JavaScript, and HTML/CSS.

---

## Contributors: 
-Olivia Bertinelli: Backend Developer\
-Kalee Burchett: Frontend Developer\
-Alan Emerson: Testing and Documentation


##  Features

- Browse the full coffee shop menu
- Add and remove items from your cart
- Place pickup orders easily
- Responsive, user-friendly design
- Dynamic interactivity powered by JavaScript

---

##  Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** Django

---
## Project Structure

coffeeright-ordering-system/\
├── coffeeright/  \
├── static/       \
├── templates/      \
├── manage.py\
├── requirements.txt\
└── README.md

---

##  Setup Instructions

Follow these steps in GitBash, Command Prompt, or PowerShell to run the project in a local environment:

### 1. Clone the Repository
```bash
git clone https://github.com/obertinelli/coffeeright.git
cd coffeeright-ordering-system
```

### 2. Create the Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Dependencies
```bash
python manage.py migrate
```

### 5. Run the Server
```bash
python manage.py runserver
```
**open your browser and go to http://127.0.0.1:8000/**

---

## License
This project is for educational purposes and is not intended for commercial use.
