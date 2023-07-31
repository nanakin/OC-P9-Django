# `LITReview` Front-End and Back-end Project using Django

## Preamble
This website was designed for a school project with specific requirements and fixed constraints.
It was developed in a limited period of time and in this context this project is not intended
to evolve that much once finished. This project is not open to contribution.
The following need is fictive.

## About the project

<img src="https://github.com/nanakin/OC-P9-Django/assets/14202917/d79cb60d-c528-47cf-b434-de00d3fb0234" alt="LITRevu logo" width=500>

### Project context
I recently joined a young start-up named LITRevu (referring to literature reviews) as Python Lead Developer. 
The start-up goal is to develop (and commercialize) a web based product allowing a community of readers and writers to 
**publish and request reviews** of books (or articles).

### About the website functionalities
The web application allows to:
- consult reviews and tickets (request for reviews),
- post tickets (+ edit and delete),
- post reviews (+ edit and delete),
- follow authors/reviewers (+ unfollow),
- signup (+ login and logout).

### About the application technology, design and compliance
The application: 
- is using [Django](https://www.djangoproject.com/) (open-source python-based web framework that follows the Model–Template–Views architecture)
- is not using Javascript,
- is not using CSS framework,
- is valid [W3C HTML](https://validator.w3.org/) and [W3C CSS](https://jigsaw.w3.org/css-validator/),
- is compatible with small screens,
- is following [WCAG](https://wcag.com/) (Web Content Accessibility Guidelines)

The python code:
- is following Django's best practices,
- is [PEP8](https://peps.python.org/pep-0008/) compliant ([flake8](https://pypi.org/project/flake8/) valid),
- is [Black](https://pypi.org/project/black/) formatted.

### Screenshots

<img src="https://github.com/nanakin/OC-P9-Django/assets/14202917/56adafc0-5d23-4321-9685-ceaf1e24f860" alt="main" width="700"/>
<img src="https://github.com/nanakin/OC-P9-Django/assets/14202917/a0f45511-f7f7-4c05-be99-30f5e5255e27" alt="edit-review" width="700"/>
<img src="https://github.com/nanakin/OC-P9-Django/assets/14202917/6eb5dcfd-04aa-44e2-bc5b-9f7ba3fbd1c0" alt="abonnements" width="700"/>

## Technology

<img src="https://github.com/nanakin/OC-P9-Django/assets/14202917/6552e943-82a4-4fda-b8c9-9ad0775adcf5" alt="python-django" width="150"/>

This application was tested with python `3.11` version, with pip `23.2`, and django `4.2`.
The development environment was macOS `13.4` and firefox `115`.

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/nanakin/OC-P9-Django.git django-project
   ```
2. Move to the project directory:   
   ```sh
   cd django-project
   ```
3. Create a virtual environment (optional):
   ```sh
   python3 -m venv venv
   ```
   and activate it:
   ```sh
   .\venv\Scripts\activate  # windows
   source venv/bin/activate  # unix and macOS
   ```
4. Install project dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Move inside the django project:
   ```sh
   cd lit_review
   ```
6. Create migration files (corresponding to database structure):
   ```sh
   python3 manage.py makemigrations
   ```
7. Launch the server:
   ```sh
   python3 manage.py runserver
   ```
8. Open http://127.0.0.1:8000/ on your web browser.

## Use existing user

You can login with a pre-existing superuser `Jangolito` with password `Djan-g0!`.
