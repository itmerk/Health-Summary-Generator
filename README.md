# Health-Summary-Generator

## Objective

The project aims to reduce the time veterinarians spend reviewing a patient’s medical records before appointments.

## Problem Statement

Veterinary patients often have extensive medical histories, including diagnostic details, lab reports, vaccination records, and more. These records are typically stored as unstructured PDF files, sometimes spanning hundreds of pages. Currently, veterinarians must spend 30-40 minutes manually reviewing these documents to find relevant information, which reduces overall clinic productivity.

## Proposed Solution
We propose an AI-based information extraction system that efficiently analyzes large volumes of medical records and generates a structured summary document.

## Software tools used:
* Microsoft Visual code
* Python 3.12.2
* Google Gemini API key (OPEN-Source)

## Create a new virtual environment
python -m venv myenv

## To Activate the virtual environment
myenv\Scripts\activate

## To Deactivate the virtual environment
deactivate

## Create Google Gemini API Key using below link
https://ai.google.dev/gemini-api/docs/api-key (Make the Key screatly do not share it)

## Using environment variable we can hide the key and easy to access with command

To set the environment variable permanently (so it persists across sessions), you can use the System Properties window:

* Right-click on This PC or Computer on the desktop or in File Explorer.
* Click Properties.
* Select Advanced system settings on the left.
* In the System Properties window, click Environment Variables.
* Under User variables (for setting it just for your user), click New.
* Enter API_KEY as the Variable name and your actual API key as the Variable value.
* Click OK to save.

## Install all requirements using below command

```bash
  pip install -r requirements.txt
```
