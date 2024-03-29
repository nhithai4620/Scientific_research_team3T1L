# Django Vietnamese personal card OCR
## Installation
Creation of virtual environments is done by executing the command venv:
```bash
python -m venv venv
```

That will create a new folder env in your project directory. Next activate it with this command on mac/linux:
```bash
source venv/bin/active
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements:
```bash
pip install -r requirements.txt
```

Go to this [link](https://1drv.ms/u/s!Avsw2PR5gprjicdb8kstRQchzCnsiw?e=RH2KDb) to download data file for PyTorch and paste it to this following directory:
```directory
.../django-ocr-app/ocr
```

In the project folder, create **media** folder and its subfolders as structure below:
```
├───media
│   └───images
│       ├───driving-license
│       ├───id-card
│       └───student-card
```

## Usage
Run the project with this command. Then open http://localhost:8000 in your borwser to see the website.
```bash
python manage.py runserver
```