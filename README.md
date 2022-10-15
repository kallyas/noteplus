<!-- Add logo at the center with the title of this app -->
<p align="center">
  <img src="./static/assets/images/logo.png" alt="Logo" width="80" height="80">
    <h3 align="center">Note Plus</h3>
    <p align="center">
      Create and Manage Your All notes in one place
      <br />
    </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

<!-- ABOUT THE PROJECT -->
## About The Project

[![Notes Plus](https://user-images.githubusercontent.com/60466044/195991507-7902e8d5-06f8-45ac-9262-b14f963a7ab2.png)
](https://noteplus-production.up.railway.app/)

Notes Plus is a simple note taking app that allows you to create and manage your all notes in one place. You can create notes, edit notes, delete notes, search notes, and share notes with your friends.

### Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
* [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/)
* [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)
* [Flask-Mail](https://pythonhosted.org/Flask-Mail/)
* [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/)
* [Flask-Gravatar](https://flask-gravatar.readthedocs.io/en/latest/)
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

```sh
git clone https://github.com/kallyas/notesplus.git
```

### Prerequisites

To run this project, you will need to install the following:

* Python 3.6 or higher
* pip
* MySQL or MariaDB or PostgreSQL

### Installation

1. Clone the repo
```sh
git clone  https://github.com/kallyas/notesplus.git
```
2. Install Python packages
```sh 
pip install -r requirements.txt
```
3. Create a database and update the database URI in `config.py` file
4. Run the following commands to create the database tables and run the app
```sh
flask db init
flask db migrate
flask db upgrade
flask run
```

<!-- USAGE EXAMPLES -->
## Usage

1. Register a new account
2. Login to your account
3. Create a new note
4. Edit or delete a note
5. Search for a note
6. Share a note with your friends


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Kallyas - [@kallyas](https://twitter.com/kallyasl)

Project Link: [Demo](https://noteplus-production.up.railway.app/)
