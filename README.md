[![DOI](https://zenodo.org/badge/175026051.svg)](https://zenodo.org/badge/latestdoi/175026051) [![Build Status](https://travis-ci.com/erickmartins/autoQC_extras.svg?branch=master)](https://travis-ci.com/erickmartins/autoQC_extras)



autoQC_extras - plotting utilities for autoQC 


Continuing development by Erick Ratamero, experimental input and testing by Claire Mitchell  
https://www.warwick.ac.uk/camdu


==========================================================================================

Usage Instructions:

Run plot_history.py. It will look for "summary_PSF.csv" and "summary_power.csv" files inside
your folder of choice, and use the folder name where they are as the date (suggested folder names
should follow the format YYYY-MM-DD). It will generate Plotly HTML files that can be uploaded
to a website for interactive plots.  

If you want lines for the axial/lateral diffraction limits, place a file named "resolution_limits.csv"
in the parent directory above the directory you select for plotting. The suggested folder structure
is as such:  

main folder -> microscope folder -> date folder -> summary_PSF.csv  

resolution_limits.csv should go on the main folder, date folders should follow the YYYY-MM-DD format.  



==========================================================================================




