# Send your RSS news to your Kindle

`kindle-newspaper` is a little Python script that will read a list of RSS news, package them as a MOBI/EPUB file, and then send it to your kindle via kindle mail address and Amazon's whispersync.

**This script is based on code from
<br>
`https://github.com/anteprandium/news2kindle` and
<br>`https://github.com/pictuga/morss` aims to solve some of the problems faced when using anteprandium's script:**

1. The original script only downloaded summaries of provided rss feeds. This made the entire process redundant since to read an interesting article you'd need to redirect yourself to the host website in the end. The entire point of such a utility, in my opinion, is to provide a complete newspaper experience on your kindle.

2. Anteprandium writes in their bio that this script is meant for people with know-how. This author disagrees with such Gatekeeping, believing that everyone who owns a kindle should be able to enrich their reading experience regardless of their prior programming experience.
   <br>In that effort I have tried to write an exhaustive setup guide and have also addressed the MANY bugs and changes I had to make to get this project up and running.

_Caveat_: If your MOBI file gets bigger than 25MB (easy if you have a lot of RSS sources), amazon will refuse to whispersync to your device. Can't do anything about it.

## Under the hood

This is a simple Python script that will download all your RSS news, package them as an EPUB first using `pandoc`, and then generate a Kindle file from that. This is a very roundabout way to do things, but it turned out to give the best results.

Then, it will sleep for 24 hrs (adjustable) and do it all over again. The idea is to leave the script running in some server, and comfortably have your news delivered to your Kindle, once, at your leisure, so you can get the news and go back to your more pressing matters.

# Installation

**Note: This script has only been tested on UBUNTU and UBUNTU MATE for now**

First, Change into the **cloned github repo**

### 1. Install docker

`sudo apt install docker`

### 2. Setting up docker permissions

    sudo usermod -aG docker $USER
    newgrp docker

### 3. Setting up environment file

    nano ./config/news2kindle.env

If you're using Gmail, you'd need to setup [Google App Password](https://support.google.com/accounts/answer/185833?hl=en) and use them for `username, password` fields in the file.<br>
If you're using other service providers, then their process would vary.<br>

    EMAIL_SMTP=smtp.gmail.com
    EMAIL_SMTP_PORT=465
    EMAIL_USER=username@gmail.com
    EMAIL_PASSWORD=password
    EMAIL_FROM=username@gmail.com
    KINDLE_EMAIL=username@kindle.com
    UPDATE_PERIOD=24
    FETCH_PERIOD=24
    LIM_ITEM=20

`mv ./config/news2kindle.env` to where you store your environment variables.
For instance, I store mine at `/etc/environment.d/`

### 4. Setting up feed

    nano ./config/feeds.txt

The RSS feeds are listed in a file called `feeds.txt`, one per line. The modification date of `feeds.txt` will be the starting date from which news are downloaded.

### 5. Change into the **cloned github repo** and execute following docker commands:

    docker build -t news2kindle .
    docker run --env-file </path/to/env/file/> news2kindle

where the `.env` file contains all the environment variables defined in [news2kindle.py](src/news2kindle.py).

# Custom configurations

There are a couple custom change to the script as per your own liking. These would however require changes to the script.

It is advisable to use a text editor like vs-code. But for the purpose of this documentation the commands will be using `nano`.

### 1. Getting all posts posted within an X-hour period

        nano ./config/news2kindle.env

change `FETCH_PERIOD=24` to set up a time range.
<br>This will fetch all the posts from the rss feed posted within now and the last X-hours.

### 2. Setting a maximum number of posts to fetch

    nano ./config/news2kindle.env

change `LIM_ITEM=20` to set up a max-number of posts to fetch.

### 3. Changing the send period

    nano ./config/news2kindle.env

Change the `UPDATE_PERIOD` field to setup time to wait in hours before sending the next feed.

**Note: Remember to rebuild the docker again.**

# Acknowledgements

This author would like to thank anteprandium and pictuga for their respective scripts.

# Contribution

You can contribute in many ways!

1. You can test the script in your own system and add steps.
2. You can report bugs and issues.
3. Better yet, you can **SOLVE** and document the bugs you come across.
4. You can help optimising the code. I am not experience in docker and so Im sure there are redundancies in my code.
