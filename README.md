# guestready-test
## Setup

The first thing to do is to clone the repository:

```sh
$ git clone git@github.com:khchine5/guestready-test.git
$ cd guestready-test
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/reservation/previous-reservation/`.

To the get the view with the table of Reservations with "previous reservation ID".

## Test
To run test you can use the following command:

```sh
(env)$ pytest
```
