# ARM DEV SUMMIT - WATER RESOURCE MONITORING (WATER LEVEL) - Host: Jason Kabi
### :one: What we intended to handle during these session

### 1. :point_right: Anomaly detection using :link: [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
**To run the notebook available you need to setup a python environment**
### 2. :point_right: If you have an environment that has the basic python modules installed, You can use it to run the notebook provided (numpy, Matplotlib, Pandas, Scikit-Learn)
### 3. :point_right: How to setup the environment

#### :one: Software Environment
 To be able to run the notebooks in this session, do the following
1. Download and install python from [python.org](python.org). Remember to link it to your path.
2. Clone this repository and cd into it - (**anomaly-detection folder**)
3. Create a [virtual environment](https://docs.python.org/3/tutorial/venv.html)
On Linux `python3 -m venv iot-env` or On Windows `python -m venv iot-env`
4. Activate it
On Linux
`source iot-env/bin/activate`
On Windows
`iot-env\Scripts\activate.bat`
5. Update pip `pip install --upgrade pip`
6. Install the requirements
`pip install -r requirements.txt`

#### :two: After setting up the environment, fire up the notebook by typing jupyter notebook on the command line.
**Green Light** :battery: 

OPTION 2: :arrow_forward: Google collab 
Link :link:[Anomaly_Detection_Notebook_Link](https://colab.research.google.com/drive/1bwZrGOH0iHLxnymcJF7hNrlXdFgVsi1Q?usp=sharing)

:arrow_right: Loading up the dataset  

- Click on the files icon on the side bar shown below.

![cover page image](/assets/img/file1.PNG)

- Click on the upload button aned you will be prompted to upload a file.
- Select the three datasets from the repo you cloned (in the data folder) and upload it.

![cover page image](/assets/img/file2.PNG)

- Right click on the dataset samples to copy the path.
- Paste it on the *dataset import slots* cell of the notebook

![cover page image](/assets/img/file3.PNG)

- Run the notebook :battery: **green light**

#### :three: water-level data visualization webapp.
- The following is a link to the water level data webapp.

Link :link:[waterlevel_webapp](https://water-monitoring-258811.wl.r.appspot.com)