# ServiceCreed
Course Project for CSN-291

## Setup 
- Clone the repo
    ```bash
	git clone https://github.com/achintyanath/ServiceCreed.git
	cd ServiceCreed
	```
- Create a virtual environment (Make sure python is installed in your machine)
    ```bash
    sudo apt install python3-venv
    python3 -m venv env
    source env/bin/activate
	```

- Install all the requirements and dependencies
    ```bash
    pip install -r requirements.txt
	```

- Start Django Server
    ```bash
    cd backend
    cd python manage.py makemigrations
    cd python mangage.py migrate
    cd python manage.py runserver
	```



