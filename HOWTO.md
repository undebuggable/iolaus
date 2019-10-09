Auto formatting
--------------

Enable auto formatting of Python in PyCharm with Black or Save Actions

### Auto formatting with Black

Configure the [auto formatting](https://black.readthedocs.io/en/stable/editor_integration.html) of Python code with Black in PyCharm.

The Black configuration is stored in the file [`pyproject.toml`](https://black.readthedocs.io/en/stable/pyproject_toml.html).

### Sorting of imports with Save Actions

Install the [Save Actions plugin](https://plugins.jetbrains.com/plugin/7642-save-actions/reviews).

The Save Actions configuration stored in the file `.idea/saveactions_settings.xml`.

Update the PyCharm settings:

Preferences ➜ Save Actions ➜ Activate save actions on save

Preferences ➜ Save Actions ➜ Optimize imports

Save Actions supports auto formatting of the source code as well.

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
