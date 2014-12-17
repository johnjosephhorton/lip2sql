lip2sql
=======

This command line tool parses resumes from LinkedIn. 
The script takes a folder with PDF files, goes through every one of them looking for Experience and Education sections, extracts all data that is found there and creates a database with following structure:

![alt tag](https://cloud.githubusercontent.com/assets/2708297/5460886/97e635dc-8577-11e4-869c-fe1e3ea08a85.png)
            
Requirements
============
Python 2.7

PDFMiner

Install 
=======
Clone the repository to your home directory and change into that directory, then run

    python setup.py install 
   
Usage
======
    
    lip2sql -i inputfolder -o outputfile.sqlite

Script will search 'inputfolder' for PDF files and will create a database with 'outputfile' path.

