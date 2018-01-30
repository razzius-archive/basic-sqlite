# [Python](http://python.org) + [SQLite](http://sqlite.org)

Interactive guide:

## Install python

Refer to [The Hitchhiker's guide to Python](http://docs.python-guide.org/en/latest/starting/installation/)

## Run a python script

```python
# script.py
import sys

print(sys.argv)
```

## Install SQLite

See the notes in PyClassLessons[https://github.com/razzius/PyClassLessons/blob/master/course/sqlite3.md#the-sqlite-relational-database-format]

- On OSX with Homebrew, type brew install sqlite
- On Debian/Ubuntu or similar Linux distributions, type apt-get install sqlite
- For Centos/Fedora, use yum install sqlite
- For anything else, ask the instructor :)

## Create table

!(Alan Turing)[https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Alan_Turing_Aged_16.jpg/220px-Alan_Turing_Aged_16.jpg]

> I propose to ask the question: what if this class were an application?

```sql
-- schema.sql
CREATE TABLE IF NOT EXISTS "users" (
    "pk" INTEGER PRIMARY KEY,
    "username" varchar(255) unique,
    "fav_color" varchar(255) DEFAULT NULL
);
```

## Manually do an insert using the sqlite command

Connect to sqlite from a command line with the `sqlite3` command

```sh
$ sqlite3
sqlite> .open users.db
sqlite> .read users_schema.sql
sqlite> insert into users(username, fav_color) values ("razzi", "lightblue");
sqlite> select * from users;
```

## Connecting from python

Now we'll edit our script.py to open a database connection.

```python
# script.py
import sqlite3

with sqlite3.connect('users.db') as conn:
    c = conn.cursor()

    values = ['razzi', 'lightblue']

    insert_statement = """
    insert into users values (?, ?);
    """
    c.execute(insert_statement, values)
```

We can parameterize it with command line arguments:
```python
# script.py
import sys
import sqlite3

with sqlite3.connect('users.db') as conn:
    c = conn.cursor()

    values = sys.argv[1:3]

    insert_statement = """
    insert into users values (?, ?);
    """
    c.execute(insert_statement, values)
```

```python
# read_from_database.py
SELECT_STATEMENT = "SELECT * FROM users"
c.execute(SELECT_STATEMENT)
print(c.fetchone())
print(c.fetchone())
```

## Realistic application: user landing page

Since we're working in Python, we can easily spin up a server which reads from the data.

```python
from bottle import route, run


@route('/')
def index():
    return """
    <title>Python Class App</title>
    Here's some info about members of the class
    """


run(reloader=True)
```
