# fetch_rewards_exercise

## Description

My submission for Fetch Rewards' coding exercise.
This project is a web service that accepts HTTP requests and returns reponses based on the conditions based the conditions outline in the Fetch Rewards Coding Exercise.

## Getting Started

### Dependencies

In order to run this web service on your local machine, please have the following technologies installed:

- Python 3.8 or greater. You can learn how to install [here](https://www.python.org/downloads/).
- Django 4.0.4. You can learn how to install [here](https://www.djangoproject.com/download/).
- Django REST framework. You can learn how to install [here](https://www.django-rest-framework.org/#installation)

### Installing

- To install this respository onto your local machine:

#### Direct Download:

- Click on the green button labeled 'Code'
- Click on Download ZIP
- Extract the ZIP file to anywhere onto your

#### Using Git (Learn more about Git [here](https://vnestor.github.io/personal-blog/my-second-post/)):

- Click on the green button labeled 'Code'
- Copy the remote URL under HTTPS
- In a new terminal shell:
  - Go into a folder where you would like to clone the respository.
  - Type the following command:

```
  git clone <remote_URL>
```

## Executing program

Once installed on your local machine, in a terminal shell navigate into the repository folder.

```
    cd fetch_rewards_exercise
```

- Run the following commands to ensure Django is executed corretly:

```
    python manage.py makemigrations execise_api
```

```
    python manage.py migrate
```

```
    python manage.py runserver
```

- If succesfully installed and executed, you will now be running the web service on your local machine.
- To delete all the data initialized, run the following command:

```
    python manage.py migrate execise_api zero
```

### Important Notes:

- By default Django should run the development server at 'http:127.0.0.1:8000/'
- If this is not the case for you, Django will show you where is it running:

```
    System check identified no issues (0 silenced).
    April 28, 2022 - 15:39:49
    Django version 4.0.3, using settings 'fetch_rewards_exercise.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
```

- Wherever the development server is started at, should be where you direct your requests to.

- This repository will be initialized with the sample data provided by Fetch Rewards
- If will have not called the /spend-points route.
- Calling the /spend-points route will the first time this route is called.
- To delete all the data initialized to store new data, run the following command:

```
    python manage.py migrate execise_api zero
```

### How to Use the web service

- Because this is a Django app, the example shown will be done in python.

#### Available Routes

**Points**

```
fields:
    {
        id:Integer,
        payer: String,
        points: Integer
    }
```

GET:

- /points

**Transactions**

```
fields:
    {
        id:Integer,
        payer: String,
        points: Integer,
        timestamp: Date
    }
```

GET:

- /transaction

**Add Transactions**

```
fields:
    {
        payer: String,
        points: Integer,
        timestamp: Date
    }
```

POST:

- /add-transaction

**Spend Points**

```
    fields:
    {
        points: Integer
    }
```

POST:

- /spend-points

### Examples

#### GET All Points

```
    import requests

    BASE_URL = 'http://127.0.0.1:8000'

    get_response = requests.get(f"{BASE_URL}/points")

    print(get_reponse.json())
```

#### GET All Transactions

```
    import requests

    BASE_URL = 'http://127.0.0.1:8000'

    get_response = requests.get(f"{BASE_URL}/transactions")

    print(get_reponse.json())
```

#### POST Transaction

```
    import requests

    BASE_URL = 'http://127.0.0.1:8000'

    new_transaction = { "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" }

    post_response = requests.post(f"{BASE_URL}/spend-points", json=points_to_spend)

    print(get_reponse.json())
```

#### POST Spend

```
    import requests

    BASE_URL = 'http://127.0.0.1:8000'

    new_transaction = { "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" }

    post_response = requests.post(f"{BASE_URL}/spend-points", json=points_to_spend)

    print(get_reponse.json())
```
