# ArchiveFiles introductions

Desktop and Downloads's files move to Archive folder which if you didn't use 7 days.

# Benefit

Your desktop and download folders keeps clean!!

# Setup

## 1.Download

`git clone git@github.com:sleepless-se/ArchiveFiles.git`


## 2.Cron setting
```
crontab -e
0 0 * * * python3 path/to/ArchiveFiles/main.py
```
**note**:Don't save ArchiveFiles on Desktop or Downloads. It'll moved to Archive folder. It'll not to work.

# Settings

You can change the keep file range date and Archive folder name from `ArchiveFiles/main.py` 

this is default settings.

```
DAYS = 7 
ARCHIVE_FOLDER_NAME = "Archive"
```