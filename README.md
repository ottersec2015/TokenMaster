# TokenMaster

A simple decimal to Base64 encoder

# How works Discord Tokens?

Discord tokens work as follows:

It is constructed by 3 parts:
The first one is the Discord ID that we have each user (the Discord ID is a unique identifier that has each account on the platform).
The second and the third are two random algorithms of letters and numbers generated automatically when making a change of password in our account (in the case of having the double factor authentication, the second and third part of the algorithm of the discord token varies around any change in the account, from a change of discriminator, to a change of email or linking a connection to our account).

# What is TokenMaster for?

TokenMaster is simply a way to discover the first part of a Discord token, either for self-interest or to play a joke on a friend, always respecting.

# How to install TokenMaster

TokenMaster is very easy to install and here are the 3 simple steps you need to fully install this script!

```console
git clone https://github.com/ottersec2015/TokenMaster/
```

```console
cd TokenMaster
```

```console
pip install -r requirements.txt
```

# How to run TokenMaster

More easy, only 1 command...

```console
py TokenMaster.py
```




Follow me in github 💤 and remember star that project and give us feedback!
