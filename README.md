## archive_ewlogs ##

Archive Earthworm log files to yyyy/jjj directories.


### Purpose/Scope ###
Clean up earthworm log directory. Can be run manually, 
or called via cron.


## Install ##

Clone source package  
`git clone http://github.com/flyrok/archive_ewlogs`

Install with pip after download  
`pip install .`

Install in editable mode  
`pip install -e .`

Or install directly from github  
`pip install git+https://github.com/flyrok/archive_ewlogs#egg=archive_ewlogs`


## Python Dependencies ##

python>=3.6 (script uses f-strings)  

## Usage/Examples ##

To see help and defaults:  
`archive_ewlogs --help`    

To see version:  
`archive_ewlogs --version`    

To run with default logdir and outdir:  
`archive_ewlogs -n`  

