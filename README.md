# deployment_interview

Peter (CTO) likes images but loves data augmentation more. He wants a way to see how typical image augmentation in our machine learning affects the images we input to the model. He codes a simple boiler-plate application for you and asks you to finish it off!

To complete the flask app you will need to do the following:

1. Download (Do not fork) the repo, upload to a new repo in your name/account.
2. Write a dockerfile for amd64 for the app.
3. Use github actions to build the dockerfile.
4. Add an image augmentation function image_augmentations.py
5. Add a test for your function
6. Improve the repo/python code/deployment in some imaginative way to show-off... Highlight this in the readme.
7. Send the recycleye team the link to your code.

Put the instructions here on how to set up/run the docker file. It should port-forward the application to run on http://127.0.0.1:8000/.

To send an image and get the app to work open a link as follows:
http://0.0.0.0:8000/?url=<image_url>
for example:
http://0.0.0.0:8000/?url=https://imgs.xkcd.com/comics/bad_code.png

# Task Completed by Christopher Yim
1) How to start the app
2) Dependencies 
3) Run down of each of the tasks

## How to start the app locally
- Go to the directory where the docker-compose.yml file is located
- Run ``` docker-compose up ``` to build and run the dockerfile

## How to visit Azure host of the app
- Hosted on: https://recycleye-image-augmentation.azurewebsites.net/
- Based on the code in this GitHub repo

## Dependencies
- Docker 20.10.10
- Docker compose 3.0

## Rundown of each task

### Write a dockerfile for amd64 for the app.
- Dockerfile was created based on python 3.10.0
- It installs all the required python packages and then runs app.py
- Was made for easier build and run by including the docker-compose.yml file

Potential improvements/changes
- Users could be added and defined as required, so that permission to read and
edit root-owned files from the host machine would be denied.
  - This would depend on whether the app is intended to be only used internally
    within the company or opened to public, in which case more thought would have
    to be put into the security vulnerabilities.
- Another change would be to add the app.config values as environmental variables
  to the dockerfile, so that it could be edited for each container, done by adding
  the code below.
  - Whether this should be done would depend on the reason the config values are being
    altered from the default. If the intention is to keep the config values the same
    for all containers then the environmental variable addition wouldn't be required.
```
ENV SEND_FILE_MAX_AGE_DEFAULT=0
#4MB Max image size limit
ENV MAX_CONTENT_LENGTH=4194304
```

### Use github actions to build the dockerfile.
- Three GitHub actions workflow was created and added in .github/workflows
- The first is docker-image.yml, which builds the dockerfile in two OS, this being
  windows and linux.
  - By adding the GitHub actions, it allows the main user to know if certain changes
    made during a Git push or pull request would prevent the dockerfile from being able
    to be built. Thus highlighting a significant error that was made and prevents the app
    from being run.
- The second is python-app.yml, which is also based on two OS, windows and linux, and it
  conducts a general lint check using flake8 and then also run the unit tests designed in
  the later section in the file tests.py.
  - Given the advantages of having GitHub actions, it made sense in addition to building
    the dockerfile to also be running general tests on the python files written for the app.     
  - Additional python tests could be added as they are created.
- The third is azure_deploy.yml, which allows the app to be deployed and on an azure server
  so that it can be viewed live. It can be accessed by the hyperlink:
  https://recycleye-image-augmentation.azurewebsites.net/

### Add an image augmentation function image_augmentations.py
- Two augmentation ideas was thought up, one is to slightly zoom into the image while the
  second is to convert the image to greyscale.
- Both ideas were initially implemented but the greyscale image augmentation seemed more 
  appropriate as instead of translational augmentations already implemented, colour 
  augmentation could highlight whether an ML model is taking advantage of colour.
  
### Add a test for your function
- Two tests were added to test the greyscale function
- The first is to ensure that the size of the original image isn't altered during the image
  augmentation
- The second is the check that the image output from the function is actually greyscale. This
  is done by looking at the RGB values of each pixel and confirming they are the same.
   - For this test, another method could have been implemented as shown by the code below.
    The downside of this test is that it assumes greyscale from the number of colour bands
     which wouldn't be the optimal test.
    
```
# Another method of testing for greyscale, by assuming only one colour band exists 
self.assertEqual(len(test_image.getbands()),1,"Should have only 1 band") 
```

### Improve the repo/python code/deployment in some imaginative way to show-off
- Improvements on app.py
  - Comments in line 6 and line 14 of the original app.py changed to reflect actual functionality
  - As mentioned in the dockerfile, the two app.config values can be defined in an external file.
    This depends on the reason the values were changed and whether the value should be kept the 
    same for every app server or changed depending on the situation.
  - Two new html pages, error_handling.html and image_augment.html were added to handle two 
    situations found.
    - The first thing is without adding a URL link, it would lead to an error as
      the request.arg.get would fail. When the image URL is empty, it would lead to the new
      index.html page giving instructions on how to use the app.
    - If an image URL is added, then the image_augment.html page would load with one of the random
      augments added to the image.
    - If any exceptions are thrown, such as a URL link that doesn't work, or a URL link that isn't
      just an image, then an error_handling.html is displayed, which highlights the fact something
      is wrong but also the error message.
  - The print(image_url) was removed. If it is required for debugging use then it should be sent to
    a logging function, or a debug log.
  - There are vulnerabilities of using a GET request method and if possible should consider certain
    protections such as CSRF protection if required.
  - All files that are given through the URL link is currently being stored as a jpg which could
    lead to a loss of quality or information if the image is originally a .gif or a .png. This 
    would depend on whether the image is then fed to an ML model, in which case consistency in 
    image file format would be preferred.

- Improvements on image_augmentations.py
  -  In general there wasn't any improvements that I would recommend, the only edit being
    to add an annotative parameter describing the return type of each of the functions using
     ```->```