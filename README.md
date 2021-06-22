# Fake-News-Detector-Web-Application
A Django and React JS Web Application which detects Fake News Articles by predicting their Spam Content using a CNN based Deep-Learning Model trained on Fake News Dataset from Kaggle.
The application can be found live at [React Fake News Detector](https://obscure-mountain-05331.herokuapp.com/).

The Backend of the Application was made using Django and the Front-End was made using React JS. This branch contains the files for Backend. The files for Backend can be found in the Main Branch.

### Directory Structure

The directory is a ***Django*** web application set-up for hosting on *Heroku* servers. The description of files and folders can be found below:

  1. **Backend** - This folder contains all Files needed for Django Application.
  2. **requirements.txt** - Containing all dependencies of the project.
  3. **nltk.txt** - Containing all NLTK library needed dependencies.
  4. **Procfile** - Needed for Heroku Deployment.
  5. **fake.csv** - Kaggle Dataset used in the Project.
  7. **my_model7.h5** - Glove + CNN Model used for Prediction.
  8. **Glove_Embedding_+_CNNs.ipynb** - Notebook used for training the Model on the dataset.
  9. **Templates** - This folder Contains the HTML files used for Django Application's display. 
  10. **Working** - This Folder has some Screenshots of the live Application.

### Approach

After experimentation on several cominations like Self Trained W2V + CNNs, Self Trained W2V + CNNs with Attention, Glove Embedding + CNNs, it was observed eperimentally that
Glove Embedding + CNNs gave the best result. Hence, this model's weights were saved and used for the Web Application. 
