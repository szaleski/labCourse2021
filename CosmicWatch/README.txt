This folder contains all scripts and measurements that have been done until June 14th 2021. This readme
provides a short overview of the folder contents:

/OLED/OLED.ino: Arduino sketch for the CosmicWatch with an OLED screen
    -the initial commit is directly from the MIT github repository
    -further commits: removed detector name from output (problems with python), 
                    converted milliseconds to seconds and changed output format

/PIN_Diode/PIN_Diode.ino: Arduino sketch for the PIN diode from lab course experiment T7


compare.py, COMreadout.py: Python scripts to run PIN diode and CosmicWatch simultaneously


COM5data.txt, COM6data.txt: leftovers produced from COMreadout.py (see according measurements section)


evaluate.py: Python script for evaluation of time differences between measured cosmic events


measureRate.py: Script initially created to replace an OLED screen

/measurements

    /PIN-Cosmic_comparison: Results for simultaneous measurements of PIN and CosmicWatch:

        - filetypes: (ms-dos) .csv, readable from excel
        - the data was captured using compare.py as starter script
        - third and forth column in the first row contain measurement length and resulting rate
            BUT: due to unknown errors in the storage concept not all events where stored at the end.
                Thus the correct rate should be calculated from the time stamp of the last events
        - original script architecture was to let COMreadout print only to stdout which is 
            stored in a readable buffer file. On my windows 10 laptop this method seemingly only
            supplies limited storage so that much of the CosmicWatch data from each measurement was lost.
            Storing the output additionally in a file did not help much further as comparison of measurement
            time and last timestamp show
    --> suggestion in case a similar measurement needs to be taken again and the same problem occurs: 
        Approach with (local) websockets which can handle this kind of asynchronous behaviour quite well

    /CosmicWatch2_tests

        - filetypes: (ms-dos) .csv, readable from excel
        - these files where created without a python script by copying the output from the Arduino IDE's
            serial monitor into a textfile, which was then converted by excel to .csv. This was only useful
            to avoid changing evaluate.py and does not need to be continued.

    /differentFloors: With these measurements the measured rate can be compared between ground level
                        (lab course rooms) and 5th floor
        - lowerfloor.txt: measurement with CosmicWatch1 at Stern Gerlach room
        - upperfloor.txt: measurement with CosmicWatch2 at 5th floor, stopped working after 26mins
        - upperfloor_working.txt: measurement with CosmicWatch1 at 5th floor, no problems
        - gemlab.txt: measurements taken with CosmicWatch1 at Gemlab during setup for coincidence

