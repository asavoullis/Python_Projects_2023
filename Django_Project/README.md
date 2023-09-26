# Django Project README

## Project Overview

The project currently consists of two apps: `myapp` and `playground`.
It includes URL mappings to views, uses templates for rendering HTML pages, integrates the Django Debug Toolbar feature for debugging, and provides custom tools within the Django admin page.

This Django project, developed by Charilaos, is a web application created to enhance and expand skills in Django, Python, Full Stack Development.

## Features

- **Two Apps**: The project includes two Django apps:

  - `myapp`:
  - `playground`

- **URL Mapping**: URLs have been mapped to views in both apps to handle various functionalities.

- **Templates**: HTML templates are used for rendering dynamic web pages. You can find the templates in the respective app directories.

- **Django Debug Toolbar**: The project integrates the Django Debug Toolbar to aid in debugging and profiling your application. This powerful tool provides insights into your project's performance and helps identify issues.

- **URL Mapping**: URLs have been mapped to views in both apps to handle various functionalities.
- **Templates**: HTML templates are used for rendering dynamic web pages. You can find the templates in the respective app directories.
- **Django Debug Toolbar**: The project integrates the Django Debug Toolbar to aid in debugging and profiling your application. This powerful tool provides insights into your project's performance and helps identify issues.
- **Database Model**: A simple database model has been created to store and manage data relevant to your project. Describe the model and its purpose here.
- **Display Dynamic Data**: The project showcases the ability to display dynamic data from the database model in your templates. Explain how this is achieved and where users can see this dynamic content.
- **Admin Page Tools**: Custom tools have been added to the Django admin page to assist in managing your application. These tools provide additional functionality tailored to your project's needs.

## Getting Started

To run this Django project, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/asavoullis/Python_Projects_2023/tree/ac60cc02c3d4c09f9b6b8af23a55bc8c639e0d34/Django_Project
   ```

2. Navigate to the project directory:

   ```bash
   cd Django_Project
   ```

3. Install project dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations to create the database schema:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver 9000
   ```

6. Open your web browser and visit `http://localhost:9000/` to access the project.

## Usage

- Describe how to use the different features of your project.
- Provide examples or screenshots if necessary.
- Explain how to navigate through the apps and use the admin page tools.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.

2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add your commit message here"
   ```

4. Push your branch to your fork on GitHub:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Create a pull request from your branch to the `main` branch of this repository.

## License

This project is licensed under the Charilaos Savoullis.

## Contact

- If you have questions or need assistance, feel free to contact me.
