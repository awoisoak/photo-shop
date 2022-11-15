# photo-shop
Simple web server created with Python and Flask to be used in different [devops projects](https://github.com/awoisoak/devops-sandbox).
- It will attempt to connect to a DB to retrieve the images, if it can't connect to it it will retrieve them locally.
- By default it will attempt to connect the DB in the localhost. Set a database url by setting an environment variable DATABASE_URL. 
- If it can not fin to the DB, it will grab the images locally.

![photo-shop](https://user-images.githubusercontent.com/11469990/198861198-b9af6107-7f2f-4533-82f7-02a0fcd72d3b.png)

A Docker image is built and uploaded to [Docker Hub](https://hub.docker.com/repository/docker/awoisoak/photo-shop) automatically on every push to the repository.

Use `awoisoak/photo-shop:main` to pull a stable build or 
`awoisoak/photo-shop:latest` to pull the last commit at any branch. 
If interested on a specific branch it can be pulled as well by using it as a tag.