# author: M. Maldonado, S.Trehan, A. Muhammad
# date: 2020-01-18
'''The following scripts downloads zip files, from a determined URL , unzips them and saves into a determined file path.
This script takes a url to the data and a 
file location as the arguments.
Usage: data_download.py --url=<url> --destination=<destination>

Example:
    python scripts/data_download.py --url="https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip" --destination="data/"

Options:
url=<url> The url containing the zip files
--destination=<destination>  Path where files are to be saved
'''


import requests, zipfile, io, pytest
from docopt import docopt
opt = docopt(__doc__)

## Test

def test_function():
    '''
    Tests if the given url for downloading the file is up.
    '''
    r = requests.head(opt["--url"])
    try:
        assert r.status_code, 1
    except AssertionError as e:
        e.args += ("Inputed Ulr is not Up")
        raise

# test function runs here
test_function()



def main(url, destination):
    """ 
    This function downloads , unzips and saves a .zip from a determined URL into a determined file path.
    
    Parameters
    ----------
    url: str
        The Url where the zip file to be downloaded/extracted/saved is located.
    
    destination: str
        Destination's local path, where unzipped files are to be saved.
    
    Returns
    ---------
    None
    """



    raw_data = requests.get(url)
    zip_file = zipfile.ZipFile(io.BytesIO(raw_data.content))
    zip_file.extractall(destination)
    print("File(s) extracted into", destination)
#Calling main function
if __name__ == "__main__":
    main(url=opt['--url'], destination=opt['--destination'])
