To build the app, go to the directory where docker file is present and use below command

``docker build -t pottery .``

To run the container without any volume association to host 
``docker run -it -p 8080:5000 pottery``

If you want to associate a host volume to maintain persistance
``docker run -it -p 8080:5000 -v /Users/venkat.chinni/Documents/mongo_storage/data/db:/data/db pottery``