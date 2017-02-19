from subprocess import call
call(["echo", "test"])

# simple example of running a command in shell from py
# so here is what we need to do I guess

# establish a function to connect to openVPN (in a screen?)
# > then we can use this function for all the other methods of
# > connecting, so perhaps the function is something like
# > vpnconnect(args)
# > then say we have the random script that does this:

# # random function (example)
# reads directory and counts files, lets say 100 files
# finds a random number between 1 to 100
# returns that as the corrosponding file to connect to
# calls the function: vpnconnect(random-file)

# # country function
# prompt for country code
# seach files with the country code in it and then return matches
# "There are 42 servers for US (United States), enter a number between 1-42"
# then simply call: vpnconnect(link-to-file)

# # favourites
# establish a method for creating a favourites file and then a structure
# way to interprit the file, so it could be in this form:
#
# in favourites.conf
# [USA-TOR]
# filename:us13.nordvpn.udp112223.whatever
#
# [slexvpn]
# filename: au12.nordvpn.upde3wew.etc.etc

# # favourites function (load)
# take input from command, and search favourites.conf for it
# call vpnconnect(fav filename)

# # VPN specific type function
# get type of vpn they want from the args (so say P2P), return something:
# there are 4 P2P Optimised VPN servers, please enter a number 1-42 or
# for more details (location, etc) type ?N where N is the server number.
# vpnconnect (filepath)

 # other todo
 # help page, save favourite function
 # check for existing vpn connection
 # check for dependencies, etc etc etc
