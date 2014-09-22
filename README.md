enigma2_dreambox_scanner
========================

A plex movie scanner using the ts.meta info for sreambox recorded satellite movies

This is a first attemp, with much to many debugging, to get a better insight how movie scanners interact wit the Plex Media Server.

Right now it retrieves the programm name and the year the movie was released from the *.ts.meta file, if one is provided.
This info is then added to the mediaList array, which is then passed to back to the Plex Media Scanner, doing its magic.

But in my test section, the provifed name and year seems not to be respected, and the filename is still the base for agents looking up the meta data.

Still looking for the right info to get this right.

I would love to get this work woth the standard agents looking up the metadata from the internet (The MOvie Database and/or the freebase)

Consider this code as very experimental and written by an absolute python beginner. So any tips, corrections etc are welcome.
