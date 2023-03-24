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
- Transparent background
- Production ready

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
- Python/Django
- Bootstrap
- rembg
- Dropbox

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Django

### Installation

1. Clone the repo and navigate to ```background-remover``` directory 
   ```
   git clone https://github.com/balewgize/background-remover.git
   ```
   ```
   cd background-remover
   ```
2. Install required packages (virtual environments recommended)
   ```
   python3 -m venv venv && source venv/bin/activate
   ```
   ```
   pip install -r requirements/local.txt
   ```
3. Provide credentials in ```.env```  (example in .env.dev file)
   ```
    DJANGO_SECRET_KEY=
   ```
   Use this command to generate strong ```SECRET_KEY```
   ```
   python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
4. Apply migrations and start the server
   ```
   python manage.py migrate
   ```
   ```
    python manage.py runserver
    ``` 
5. Goto http://127.0.0.1:8000 on your browser

<p align="right">(<a href="#readme-top">back to top</a>)</p>

**Note:** The project is production ready and can be easily deployed. But it requires good amount of resource to run ML models used by **rembg** in the cloud. I'm looking for ways to deploy it for free.

Thanks!
