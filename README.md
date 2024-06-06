# imageForge - Full-Stack Django Web App

## Project Overview
This is a full-stack Django-based web application that integrates the OPENAI API by using the ChatGPT 3.5 Turbo and DALL-E 2 Models to generate random and unique artwork.

## Deployment Link
This project is live! Check it out [here](https://imageforgelive-e87a9f628780.herokuapp.com/).

## Screenshots
![imageForge Homepage](static/backgrounds/project-screenshot.png)
<br />
<br />
![imageForge Generation](static/backgrounds/project-screenshot-2.png)

## Table of Contents
- [Goals & MVP](#goals--mvp)
- [Tech Stack](#tech-stack)
- [Build Steps](#build-steps)
- [Design Goals](#design-goals)
- [Project Features](#project-features)
- [Known Issues](#known-issues)
- [Additions & Improvements](#additions--improvements)
- [Learning Highlights](#learning-highlights)
- [Challenges](#challenges)

## <a id="goals--mvp"></a>Goals & MVP
The aim of this application is to create a full-stack application in the Django framework that can create random and unique images by leveraging modern tools including the OpenAI API.

## <a id="tech-stack"></a>Tech Stack
- HTML
- CSS
- Django 
- Python
- Javascript
- DALL-E 2 API
- ChatGPT 3.5 Turbo API
- SQLite / Postgres
- AWS S3 Bucket
- Heroku

## <a id="build-steps"></a>Build Steps 
1. Clone the project from GitHub:
   ```bash
   git clone git@github.com:cyberforge1/imageForge.git

2. Register for an OpenAI API key at the following [link](https://openai.com/index/openai-api/).

3. Run the `generateSecretKey.py` file in the root directory to create a Django secret key.

4. Create a `.env` file in the root directory and attach the values of the keys generated in Steps 1 and 2:

    ```plaintext
    OPENAI_API_KEY= replace-this-value
    SECRET_KEY= replace-this-value
    ```

5. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

6. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

7. Install project dependencies with pip:
    ```bash
    pip install -r requirements.txt
    ```

8. Set up and migrate the SQLite database:
    ```bash
    python manage.py migrate
    ```

9. Run the application locally:
    ```bash
    python manage.py runserver
    ```

## How To Use

To create an image, navigate to the generation page and click ‘generate’, then convert the unique prompt into unique art with a button click. The generated images can be viewed in a public gallery or a private history if logged in.

<a id="design-goals"></a>Design Goals

This project was designed to be a fun and intuitive experience for users to navigate through the application to generate unique artwork. A careful selection of backgrounds throughout the application aims to create an immersive user experience. The Gallery and User History pages were inspired indirectly by the Instagram platform.

<a id="project-features"></a>Project Features

- A collection of local data for creating randomized prompts
- A series of Python scripts that generate prompts and make API requests
- A user registration and login system
- Generation of unique prompts using the ChatGPT 3.5 Turbo Model
- Generation of unique images using the DALL-E 2 Model
- A full-stack application to display this data

<a id="known-issues"></a>Known Issues

- When a user is signed in and has a limited number of images generated, only a partial background image is displayed on the User History page.

<a id="additions--improvements"></a>Additions & Improvements

- Create mobile responsive design and mobile navbar
- Addition of delete functionality to the User History page
- Refine the Generation Page background image
- Improve styling on Login and Registration Pages
- Add a download link on modals for images
- Post images to Instagram

<a id="learning-highlights"></a>Learning Highlights

This project started as a passion project and was my first full-stack application. Through this project, I learned many fundamental aspects of web development, including how to make API calls and handle the returned data, how to set up a database, and how to deploy an application.

<a id="challenges"></a>Challenges

- One major challenge in this project was creating a system that could store the images dynamically so that many users could access and interact with the application simultaneously. This was resolved by attaching an AWS S3 Bucket.
- Another challenge was correcting the grammar and other inconsistencies of the locally generated prompts. This was resolved by making a call to the ChatGPT API.

Thanks for your interest in this project. Feel free to reach out with any thoughts or questions.

Oliver Jenkins © 2024
