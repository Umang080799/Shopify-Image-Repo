# Shopify-Image-Repo
Backend Developer Intern Challenge

# This image repository is set up as a Django web application with the funtionality:

# ADD image(s) to the repository
## - one / bulk / enormous amount of images
## - private or public (permissions)
## - secure uploading and stored images

# DELETE image(s)
## - one / bulk / selected / all images
## - Prevent a user deleting images from another user (access control)
## - secure deletion of images

# All the images are stored in image-repository/imageRepo/media/images/

# Note - Unit tests are present in folder image-repository/imageRepo/imageRepo/tests. Navigate to the location image-repository/imageRepo/ and run
# python3 manage.py test. The tests here are used to check if the image repository objects are being created correctly or not. 

## Before running the script below, ensure you have pip3 and python3 installed on your system. 

## Simply run:
# ./run.sh and the Django server will start listening on http://127.0.0.1:8000

## The script run.sh installs all the modules in requirements.txt and also prompts to enter the credentials of a superuser who can manage 
## the image repository as shown below. The superuser can also add other users explained below in the README. 

![Screen Shot 2021-05-01 at 8 49 29 PM](https://user-images.githubusercontent.com/35209670/116786928-fc664100-aabe-11eb-9dc4-cc71c775cbdc.png)

# The http://127.0.0.1:8000 will show the image repository with the following images. One can add additonal images to this repository. 

![Screen Shot 2021-05-01 at 8 29 38 PM](https://user-images.githubusercontent.com/35209670/116786616-37677500-aabd-11eb-8c53-0b4a3ac6c3c4.png)

# Go to http://127.0.0.1:8000/admin to add/delete images. You will be presented with the login page to enter the required superuser credentials. 

![Screen Shot 2021-05-01 at 8 33 23 PM](https://user-images.githubusercontent.com/35209670/116786951-1dc72d00-aabf-11eb-970e-0446ab41c134.png)

# Add images 

## The following steps are used to add images.

![Screen Shot 2021-05-01 at 8 25 21 PM](https://user-images.githubusercontent.com/35209670/116786637-641b8c80-aabd-11eb-9b02-eeda691f8a43.png)

# Delete images 

## The following can be used to delete images. The user can select the delete images option from the drop down as shown here

![Screen Shot 2021-05-01 at 8 30 42 PM](https://user-images.githubusercontent.com/35209670/116786693-b9f03480-aabd-11eb-8953-b98468286ca3.png)

## The application also asks for a confirmation before deleting

![Screen Shot 2021-05-01 at 8 30 49 PM](https://user-images.githubusercontent.com/35209670/116786729-dee4a780-aabd-11eb-84e4-9da4be074c1e.png)

## The following shows the repository after the first 3 images have been deleted 

![Screen Shot 2021-05-01 at 8 31 03 PM](https://user-images.githubusercontent.com/35209670/116786747-00459380-aabe-11eb-8c00-921d04832791.png)

# Creating other users

## The superuser (here umang) can create other sub users by choosing the 'ADD USER' button as shown

![Screen Shot 2021-05-01 at 8 31 35 PM](https://user-images.githubusercontent.com/35209670/116787011-5c5ce780-aabf-11eb-8349-2480fcd7ff7a.png)

## The following shows the setps to add a user called John Doe 

![Screen Shot 2021-05-01 at 8 32 32 PM](https://user-images.githubusercontent.com/35209670/116787141-1ce2cb00-aac0-11eb-98ba-7a9abddb84e6.png)

## The following shows the various image repository permissions that can be added for the user

![Screen Shot 2021-05-01 at 8 32 40 PM](https://user-images.githubusercontent.com/35209670/116787151-34ba4f00-aac0-11eb-90b9-3f81b1b18aa4.png)

![Screen Shot 2021-05-01 at 8 32 48 PM](https://user-images.githubusercontent.com/35209670/116787166-44399800-aac0-11eb-98e5-6f535feaa3f8.png)

## Simply log out after creating the new user and log back in with the new credentials

![Screen Shot 2021-05-01 at 8 33 17 PM](https://user-images.githubusercontent.com/35209670/116787180-603d3980-aac0-11eb-9fa9-c4c6f4fc48ed.png)

## Logging back in as John Doe

![Screen Shot 2021-05-01 at 9 03 01 PM](https://user-images.githubusercontent.com/35209670/116787224-a85c5c00-aac0-11eb-8054-caf82536318f.png)


