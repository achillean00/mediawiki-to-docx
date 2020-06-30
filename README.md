# mediawiki-to-docx
This is a quick and dirty Python script that converts all the pages in a mediawiki instance to Word documents. It also downloads all the files.

## What it does
- Builds a list of all the pages on a Mediawiki instance
- Downloads them all and converts them to Word docs, with the filename being the name of the page
- Builds a list of all the files
- Downloads them all

## Usage
### Install the dependancies
```
pip3 install mwclient pypandoc pathvalidate
```
### Edit the script
You will want to set at least `site` to reflect the site you want to pull down. You may need to change the authentication config too.

### Run
```
./mediawiki-to-docx.py
```

## Warnings
The script has fairly minimal exception handling, so if it deletes all your files, don't blame me! :)
