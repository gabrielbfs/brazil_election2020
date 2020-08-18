# brazil_election2022

## monitoring Brazilian election 2022

##### Medium

[Brazil, Jair Bolsonaro Approval .v01](https://medium.com/@gbferrada/brazil-jair-bolsonaro-approval-v01-510ad3eab8d8)

##### check out:

- 1.1-gbf-2020brazil_bolsonaroApproval ([html](https://github.com/gabrielbfs/brazil_election2020/blob/master/notebooks/1.1-gbf-2020brazil_bolsonaroApproval.html), [ipynb](https://github.com/gabrielbfs/brazil_election2020/blob/master/notebooks/1.1-gbf-2020brazil_bolsonaroApproval.ipynb))



## Motivation

> questions > data > answers

**I. Domain Perspective**

To monitor Jair Bolsonaro approval, I started with a descriptive analysis to understand the current scenario, trying to answer primary question, such as:

1. how popular is Bolsonaro's approval changing over time?
2. how Bolsonaro’s social media is changing over time?
3. could a social media engagement be a precursor variable of Bolsonaro's approval?

**II. Data Perspective**

The project follows some of the best practices in terms of DS Projects, in terms of a logical and standardized structure (option for [cookiecutter data science](http://drivendata.github.io/cookiecutter-data-science/)).

![](reports\figures\project_structure.PNG)



**how popular is Bolsonaro’s approval changing over time?**

![JairBolsonaro_approval](/reports/figures/JairBolsonaro_approval.png)



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io





<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>