# photo-shop
Simple web server created with Python and Flask to be used in different [devops projects](https://github.com/awoisoak/devops-sandbox).
- It will attempt to connect to a DB to retrieve the images, if it can't connect to it it will retrieve them locally.
- By default it will attempt to connect the DB in the localhost. Set a database url by setting an environment variable DATABASE_URL. 
- If it can not fin to the DB, it will grab the images locally.

<p align="center">
<img width="842" alt="photo-shop" src="https://user-images.githubusercontent.com/11469990/198860687-14b288ef-1e88-47ad-9806-44dadba00f2c.png">
</p>
