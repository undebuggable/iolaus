Installation
-----
Install the requirements

`pip3 install -r requirements.txt` 

Running
-----
Run the utility

`python -m hosts_pkg.merge`

This will load the files, if present, from the current directory

* `hosts.whitelist`
* `hosts.blacklist`

The result will be the files

* `hosts.merged` - merged host file
* `hosts.log` - comprehensive report on duplicated host items
