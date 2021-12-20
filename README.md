# Technical task for DevOps position
## How to run Program

* Firstly, clone the following repository: https://github.com/Thomas2499/website-healthcheck.git

* Inside the working directory, execute: ```python app.py```.

* Send the list of website addresses using HTTP POST to ```http://localhost:5000/create-env```. The response contains the website address and its newly created link for status check.


## Example
* For example, sending:
````
["http://web1", "http://google.com"]
```` 
will return:
````
{'http://web1': 'http://localhost:2499/status', 'http://google.com': 'http://localhost:2500/status'}
````

Accessing
``http://localhost:2499/status`` using HTTP GET will return **Failure**, while accessing 
``http://localhost:2500/status`` using HTTP GET will return **OK**.