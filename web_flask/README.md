This was a sub-project within AirBnB in which I began working with Flask and Jinja2. In this project, I began integrating the back-end storage engine with the web static HTML/CSS pages written earlier.

Files 0 - 6 were introductory tasks familiarizing myself with using Flask. Files 7 forward involved gradually putting together more and more complex Jinja templates based on the HBnB HTML pages.

The most complete Flask/Jinja app-template combo in this directory is defined in Flask module 100-hbnb.py and Jinja template 100-hbnb.html.

To run the Flask app, execute the following command from the root directory of the project:~ $ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost
HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.100-hbnb
