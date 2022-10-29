
# Udemy Coupons API v.1.0.0

Udemy Coupon code API v.1.0.0 is built using flask and Beautifulsoup, can be used to provide more resources to the student by integrating it in your application.
Data scrapped from the websites such as discudemy, real.discout, freeudemies etc. Sqlite3 used to make the flask application more flexible and extension of the database would be easy for anyone who wanted to upgrade this API.

## Demo Output
Postman Application:
![Image](https://i.postimg.cc/zX4qD3WM/image.png)
Browser:
![Image](https://i.postimg.cc/1X9rq9F1/screenshot-127-0-0-1-5000-2022-10-29-16-04-16.png)

## Installation

Install this api to local environment with git

```bash
  git clone https://github.com/mayurjadhav2002/Udemy-Coupons-API.git
  cd Udemy-Coupons-API
```
    
## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
   pip3 install -r requirements.txt
```

Start the server

```bash
    $env:FLASK_APP = "app"
    flask run
```
OR 
```bash
   python app.py
```




## Use in your Project

```javascript
import React,  { useEffect, useState } from "react";


function App() {
    const [user, setUser] = useState([]);

    const fetchData = () => {
        return fetch("http://127.0.0.1:5000/")
            .then((response) => response.json())
            .then((data) => setUser(data));
    }

    useEffect(() => {
        fetchData();
    },[])
        
    return (
            <ol>
                {user && user.length > 0 && user.map((userObj, index) => (
                    <li key={userObj.id} link><a  href={userObj.link} target='_blank'>{userObj.title}</a></li>
                ))}
            </ol>
        );
}
```


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.

