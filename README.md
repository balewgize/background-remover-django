<a name="readme-top"></a>

<div align="center">
  <h3 align="center">Background remover</h3>

  <p align="center">
    Remove background from images using pre-trained AI model.
    <br />
    <a href="#" target="_blank"><strong>View Demo »</strong></a>
    <br />
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Screenshot](static/images/screenshot.png?raw=true "Tomar")](#)

A web app built with Python/Django that enables users to remove background from images using pre-trained AI model. It allows users to download the final result image with a transparent background. 

It does well for most images that doesn't have messy background but I'm sure you won't expect photoshop like results :) 

### Features
- Downloadable final result
- Transparent background (PNG format)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
- Python/Django
- Bootstrap
- rembg

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Django

### Installation

1. Clone the repo
   ```
   git clone https://github.com/balewgize/background-remover.git
   ```
2. Install required packages (virtual environments recommended)
   ```
   pip install -r requirements.txt
   ```
3. Provide credentials in *.env*  (example in .env.dev file)
   ```
    DJANGO_SECRET_KEY=
   ```
4. Specify settings to use
   ```
   export DJANGO_SETTINGS_MODULE=background_remover.settings.local
   ```
5. Apply migrations and start the server
   ```
   python manage.py migrate
   ```
   ```
    python manage.py runserver
    ``` 
6. Goto http://127.0.0.1:8000 on your browser

<p align="right">(<a href="#readme-top">back to top</a>)</p>

Thanks!
