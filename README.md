# EE551-HW1

This is the first HW assignment for EE-551. The goal was to run a traceroute for 24 hours to a site across seas.

The Python script will take the log file from the traceroute bash script and go line by line to extract the ms value of the last available destination.
Using these ms values, a cdf graph was created using the matplotlib library.
