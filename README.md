## TODO List Demo App

This github repository is an application for keeping track of daily to-do tasks.
* About me: [Loi Nguyen Van](https://github.com/lloydnguyen96/) from VMOGroup

## Description

This application uses Python Flask framework for backend and simple HTML, CSS and vanilla JavaScript codes with AJAX for frontend.
This application is deployed to Google App Engine and is accessible online via [this link](https://bid21260.ew.r.appspot.com/).

## Getting Started

* Clone this repository:
```
git clone https://github.com/lloydnguyen96/ToDo.git
```
* Change current working directory to ToDo folder:
```
cd ToDo
```
* Switch to app_engine branch:
```
git checkout app_engine
```
* Create development environment:
```
conda env create -f requirements.yaml
conda activate ToDo
pip install -r requirements.txt
```
* Follow this [tutorial](https://cloud.google.com/appengine/docs/standard/python3/building-app/creating-gcp-project) to create your Google Cloud Project, Cloud SDK, etc.
* Then, follow this [link](https://cloud.google.com/appengine/docs/standard/python3/building-app/deploying-web-service) to deploy the web service on App Engine.
* You can also run server locally by entering this command:
```
flask run
```
or you can browse the running service on App Engine with:
```
gcloud app browse
```

## Help

If you have any questions, please add an issue

## Authors

* [Loi Nguyen Van](https://github.com/lloydnguyen96)
