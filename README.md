# jira-bb-clockify-cli
Jira Bitbucket Clockify automated cli tool

## Clone and run `run.py`

## Usage:

Generate an Atlassian api key.

(Optional) Generate a clockify api key. 

Edit the `config.json` file.
Set the absolute path to you're config file in `run.py`.

In you're project folder:

`python <path to>/run.py`
```
python run.py [OPTIONS] <issue number> | <issue prefix>-<issue number>
            ex: python run.py 721
                 python run.py BER-721
                 
            -p <issue prefix>  - Manually prepends issue prefix. 
                                 ex: python run.py -p BER 721
            -b <branch prefix> - Manually set a branch prefix. 
            -c                 - Don't start Clockify
```

## (Optional) For Clockify you need [Clockify CLI](https://github.com/t5/clockify-cli)

You can set the 2 env variables permanently in `.zshrc` or `.bashrc`,
depending on shell used.

You can get the project id for `clockifyProject` in the config like this:

`clockify projects 5b4dae2db079871a7925ce90`

## Set an alias

In `.zshrc` or `.bashrc`:

`alias bb="python /<path to script>/run.py"`