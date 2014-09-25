enigma2_dreambox_scanner
========================

A plex movie scanner using the ts.meta info for sreambox recorded satellite movies

This is a first attemp, with much to many debugging, to get a better insight how movie scanners interact wit the Plex Media Server.

Code seems to be running with PMS 0.9.10.x version.

Currently it has following features

* uses the ts.meta file to retrieve the prgramname and movie release year.
* If no ts.meta file is found, it will extract the programname from the ts file name.
* It only supports the dreambox enigma2 file format.
* Only Movies are supported yes.

TODO
====

* Skip series if found in the Movie Section
* Write something simulalar fot the series (in progress)
* Add support for more possible ts.meta formats, if enough examples can be found

Configuration
=============

As agent, I selected the moviedb/freebase.
Whenever I select local data, and because my database contains the original ts filenames (with the date/channel stuff)
it will select those as movie title, making everything messed up.4
Database cleanup  is something I'm looking at.


