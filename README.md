# SocialAI

The repo code can be seperated into 3 phases.
1) Data Collection
2) ML part
3) Vizualization 

The complete product is intended to run end to end with out human intervention. As pushshift api is down indefinately, these components need ot be run seperately.

Follow the following steps:
1) Clone the repo in local
2) Create a conda env and install the dependencies.
conda create --name <env> --file requirements.txt
3) run the flask applicaiton
python3 run.py
Flask generates 3 web pages.

localhost/test - Takes user search term for subreddit and the time period. After you click the submit button, a new file will be generated in the base folder.
If a file already exists then it will be rewritten

localhost/uploaded_data - After the ML algorithm generates the output, visiting this link will upload the csv (stored as df_viz.csv, can use a prameter for
future) to the flask server

localhost/viz - This page will contain the vizualization aspects

4) After the data is extracted, we run the ML model on it (Ritik will upload that file)

5) Visit /uploaded_data. The result will be uploaded to flask servers after some preprocessing.

6) Visit /viz to see the updated visualizations


