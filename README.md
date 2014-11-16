enigma2_dreambox_scanner
========================

A plex movie scanner using the ts.meta info for dreambox recorded satellite movies

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

Some observations
=================

* after upgrading PMS, force refresh only calls the scanner if something is really changed.
* To test the scanner, i had to delete the library and add it again.
* Since upgrade, the --analyze process is eating up all CPU, resulting into an unresponsive web client.
* Got loads as high as 50, running 50 analyze processes, but after couple of hours, system still works

Things I need more info on
==========================

* reduce analyze process load
  * touch jpg file ?
  * set global --nothumb flag ?
  * move the analyze process in batch to a very p[erformant server (which could be shut down when not used)
* writing an agent using the \*.eit

The .eit file of dreambox recordings
====================================

Delving in the code, it seems to me the dreambox eit files are just a part of
the Event Information Table description (ETSI EN 300 468).
It contains the data as described in  table 7 :  Event Information Section, especially the part in the first for loop, starting with the event_id field.


