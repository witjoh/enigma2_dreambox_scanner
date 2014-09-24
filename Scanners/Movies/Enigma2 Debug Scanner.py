import re, os, os.path
import Media, VideoFiles, Stack, Utils
#
# this is a start to get to learn how to write scanners
#

debugfile = '/tmp/enigma2_movie_debug.log'
debug = True

def strip_name_from_ts_file(tsfile):
    "Retrievess the programma name from a dreambox enigma2 file
     This has the form of YYYYMMDD HHMM - Channel - Programmename.ts
     code is borrowed from Enigma2 Movies.py  by Quinten
     https://forums.plex.tv/index.php/topic/68991-scanner-for-enigma2-ts-file
     Also transforms the  '_ ' to ': ' "
     base_name = os.path.splitext(os.path.basename(tsfile))[0]
     tmp_name = base_name.split(' - ' ,2)[2].strip()
     return re.sub(r'_ ',': ', tmp_name)


def Scan(path, files, mediaList, subdirs, language=None, root=None, **kwargs):
    if debug:
        logfile = open(debugfile, 'w')
        logfile.write("DEBUG_ENIGMA2 scanner called\n")
        logfile.write("Entering DREAMBOX DEBUG SCANNER\n")
        logfile.write("recvieved following parameters :\n")
        logfile.write("path parameter      : ")
        logfile.write(str(path))
        logfile.write('\n')
        logfile.write("files parameter     : ")
        logfile.write(str(files))
        logfile.write('\n')
        logfile.write("mediaList parameter : ")
        logfile.write(str(mediaList))
        logfile.write('\n')
        logfile.write("subdirs parameter   : ")
        logfile.write(str(subdirs))
        logfile.write('\n')
        logfile.write("language parameter  : ")
        logfile.write(str(language))
        logfile.write('\n')
        logfile.write("root parameter      : ")
        logfile.write(str(root))
        logfile.write('\n')
        logfile.write("kwargs parameter    : ")
        logfile.write(str(kwargs))
        logfile.write('\n')
        logfile.write("========================================================\n")
        logfile.write("               START PRFOCESSING FILES SECTION            ")

    year = ''
    genre = ''
    name = ''

    for scan_file in files:
        # Only process files having a ts extension (these are the movie files)
        if scan_file.endswith(".ts"):
            # chek then if we have the ts.meta meta file
            if os.path.isfile(scan_file + ".meta"):

                if debug:
                    logfile.write(str("found ts.meta file : " + str(scan_file + ".meta") + "\n"))

                # lookup title and year from the ts.meta file
                meta = open(scan_file + ".meta", 'r')
                lines = meta.readlines()

                if debug:
                    logfile.write("Content of the ")
                    logfile.write(str(scan_file + ".meta" + "\n"))
                    logfile.write(str(lines))
                    logfile.write("\n")

                name = lines[1].strip()

                if name:
                    # programma name is empty in the ts.meta file, so we take it from the filename
                    name = strip_name_from_ts_file(tsfile = scan_file)
                    if debug:
                        logfiel.write(str("no title in ts.meta file found, abstracted form filename : " + (name) + "\n"))
                else:
                    if debug:
                        logfile.write(str("substracted the programname " + (name) + "\n"))

                # line 3 in the meta file contains multiple formats.  In this directory we
                # assume onlu movies are to be processed
                # Most common format we have encounterd yet :
                # <genre>.<year>.<short description>  where all fields  ar not always there
                # <year>.<genre>.<short description>
                # <descripton><(year)><(duration)>
                # empty
                # <free text>

                if lines[2].strip():
                    # we do have content
                    if re.match(r'\d{4}\.', lines[2]):
                        if debug:
                            logfile.write("first RegExp matches, first field is the year\n")

                        line_array = lines[2].split('.', 2)
                        elements = len(line_array)
                        year = line_array[0]

                        if elements >= 2:
                            genre = line_array[1]
                        else:
                            genre = ''

                        if elements >= 3:
                            short_info = line_array[2]
                        else:
                            short_info = ''

                    elif re.search(r'\.\d{4}\.', lines[2]):
                        if debug:
                            logfile.write("Second RegExp matches, second field is the year\n")

                        line_array = lines[2].split('.', 2)
                        elements = len(line_array)
                        genre = line_array[0]
                        year = line_array[1]

                        if elements >= 3:
                            short_info = line_array[2]
                        else:
                            short_info = ''

                    elif re.search(r'\(\d{4}\)', lines[2]):
                        if debug:
                            logfile.write("Third RegExp matches, year after info\n")

                        pat = re.compile(r'\(\d{4}\)')
                        res = pat.search(lines[2])
                        short_info = lines[2][0:res.start()-1]
                        year = lines[2][res.start()+1:res.end()-1]
                        genre = ''
                    else:
                        if debug:
                            logfile.write("line not empty, but no match found\n")

                        # we handle this as short info
                        genre = ''
                        year = ''
                        short_info = lines[2]
                else:
                    # empty line
                    if debug:
                        logfile.write("empty line\n")

                    year = ''
                    genre = ''
                    short_info = ''
            else:
                name = strip_name_from_ts_file(tsfile = scan_file)
                year = ''

            if debug:
                logfile.write(str("the year of the movie is " + str(year) + "\n"))
                logfile.write(str("the genre of the movie is " + str(genre) + "\n"))
                logfile.write(str("the info of the movie is " + str(short_info) + "\n"))

            movie = Media.Movie(name, year)
            movie.source = VideoFiles.RetrieveSource(scan_file)
            movie.parts.append(scan_file)

            if debug:
                logfile.write("========================================\n")
                logfile.write(str(movie))
                logfile.write("\n")
                logfile.write("========================================\n")

            mediaList.append(movie)

    if debug:
        logfile.close()
