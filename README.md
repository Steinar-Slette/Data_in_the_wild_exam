# data-in-the-wild

This repository contains the code for the project for the course Data in the Wild: Wrangling and Visualising Data (Autumn 2023 - KSDWWVD1KU).

### Team Members:

Niclas Claßen (niclc@itu.dk), Marek Gala (galg@itu.dk), Manuel Knepper (mkne@itu.dk) & Steiner Slette(stsl@itu.dk)

---

# Get started

This project is split up into 4 main parts:

1. [Data collection](#data-collection)
2. [Data processing](#data-processing)
3. [Data analysis](#data-analysis)
4. [Data visualization](#data-visualization)

This README.md documents describes which files are responsible for what parts, and how to replicate our results. For a full project overview, see [Repository overview](#repository-overview).

---

# First steps

## API keys

For the data collection from 'The Guardian' and 'Pytrends' we make use of the provided APIs. Therefore you need your own API keys. The keys are stored in a .env file which can be created from the .env.sample file. The .env file should be placed in the root directory of the project.

## Python environment

We use a virtual environment to run our code. To create the environment run the following command in the root directory of the project:

```
python3 -m venv .venv
source .venv/bin/activate

# You can deactivate the environment with:
source .venv/bin/deactivate
```

To install the required packages run:

```
pip install -r requirements.txt
```

# Data collection

# Repository overview

The following tree structure shows the files and folders, their purpose and their location within this repository. The main parts of the project are described in the [Get started](#get-started) section.
