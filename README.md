## Open Source Peatio Deployed Exchange API

This is an unofficial Python wrapper for the [Peatio exchange REST API v2](https://www.openware.com/sdk/2.3/docs/peatio/api/peatio-user-api-v2.html). I am in no way affiliated with Openware Peatio Project, use at your own risk.

If you came here looking for the exchange to purchase cryptocurrencies, then go [here](https://www.binance.com/en). 

If you want to automate interactions with Peatio Exchanges stick around.

# Source code

Link to [Source Code](https://github.com/athenasaurav/Python_Peatio)

# Features
   Implementation of all General, Market Data and Account endpoints.
   Simple handling of authentication
   No need to generate timestamps yourself, the wrapper does it for you
   Response exception handling
   Symbol Depth Cache
   Kline/Candle fetching function
   Withdraw functionality
   Deposit addresses
   Trading


## On Windows

If you are using Windows as your OS then use the following steps:-
```
python -m pip install -U pip setuptools
```

Run ```pip install -r requirments.txt``` (Python 2), or ```pip3 install -r requirments.txt``` (Python 3)

Finally run ```python3 app.py``` (on Python 3)


## On Ubuntu Server

If you are using Linux as your OS then you can follow the below-mentioned steps:-

Copy all the files on the server in a folder.

Enter into the folder.

# Installing requirments

Check first if Tmux is installed or not by trying to install tmux ```sudo apt-get install tmux```

Check also if Pyhton3 Pip is installed or not. To check run the command ```sudo apt-get install python3-pip```

To upgrade pip to latest version run the following command : ```pip3 install --upgrade pip```

NOTE: pip has dropped support for Python 2 and 3.5. You will need to use a version-specific branch.
Do the following steps if your python3 version is 2 or 3.5

Step 1: This PPA contains more recent Python versions packaged for Ubuntu. Install ppa by running the following command.

```sudo add-apt-repository ppa:deadsnakes/ppa```

Step 2: Now, update your packages by running the following command.

```sudo apt-get update```

Step 3: install Python version 3.7

```sudo apt-get install python3.7```

Step 4: Install pip by running the following command.

```sudo apt install python3-pip```

Step 5 : Check Pip3 version by ```pip3 --version``` if its latest skip Step 6

Step 6: To upgrade pip3 to latest

```sudo -H pip3 install --upgrade pip```

Step 7 : Set priority of the machine to Python 3.7 we installed

```sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2```

Step 8: Run ```pip install -r requirments.txt``` (Python 2), or ```pip3 install -r requirments.txt``` (Python 3). Prefer to use Python3 always. 

# Change Config File

Update the Config file data as per this tutorial i.e [botdetails](https://github.com/athenasaurav/peatio_binance/blob/main/botdetails.md).

We will use tmux for running this program forever.

# Deploying using Tmux

Firstly use command ```tmux``` to open a tmux screen. 

By default tmux start the screen numbering from 0. You can specify name parameter to name something different the screen which will be easy to remember.

To create a Tmux session with a custom name easy to remember use the following command ```tmux new -s <sessionname or sessionnumber>```

then in the new screen run ```python3 app.py``` (on Python 3)

Voila! you bot has started running.

You can now close the SSH window or come out of screen by pressing `ctrl`+`b` and then `d`

If you would like to see whats happening in your program you can write ```tmux attach -t <screenname or screennumber>```

NOTE: we have deployed with a name ```Bot```.

To kill the screen, run command ```tmux kill-session```

To see the list of all the session, run command ```tmux list-sessions```

You can check the Tmux commands cheatsheet [here](https://github.com/athenasaurav/peatio_binance/blob/main/tmux.md)
