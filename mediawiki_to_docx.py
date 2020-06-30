#!/usr/bin/python3

import mwclient
import pypandoc
from pathvalidate import sanitize_filename

# Declare the site and bog standard login details. HTTPS is the default for mwclient
site = mwclient.Site('<sitename>',path='/')
site.login('<username>', '<password>')

# Iterate through all the pages and convert from Mediawiki format to a word document
# The filename is created from the page title and is sanitised to make sure it's valid
# Exits on an errors, which are usually caused by bad wiki syntax, but could be made to continue
for page in site.Pages:
    print ("Converting " + page.page_title)
    mwfilename = sanitize_filename(page.page_title)
    mwtext = page.text()
    try:
        pypandoc.convert_text(mwtext, 'docx', format='mediawiki',outputfile=mwfilename + '.docx')
    except Exception as ex:
        print ("*** Error converting " + page.page_title + " Exception " + str(ex))
        exit(1)
    else:
        print ("Sucessfully saved " + page.page_title + " to " + mwfilename + '.docx')

# Iterate through all the images (files)
# Uses the image name as the filename, and again this is sanitised
# Checks the imageinfo of the file as iterating all the files seems to pick up default Mediawiki files that you can't (and won't want to) download
# Only downloads if the imageinfo dictionary has content
for imagefile in site.Images:
    print ("Processing " + imagefile.base_title)
    imagefilename = sanitize_filename(imagefile.base_title)
    imageinfo = imagefile.imageinfo
    # Only download if the file is not one of the default MediaWiki ones (they don't have any imageinfo)
    if imageinfo:
        print ("Downloading " + imagefile.base_title)
        with open(imagefilename, 'wb') as fd:
            imagefile.download(fd)
        fd.close()
    else:
        print ("Skipping" + imagefile.base_title)
