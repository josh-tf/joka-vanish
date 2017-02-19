# joka-vanish - NordVPN CLI Tool

[![Python](http://i.imgur.com/Vjttl4P.png?1)](https://www.python.org/)

Vanish is a easy-to-use command line based client for [NordVPN](https://nordvpn.com/). Vanish has a range of features including selecting servers based on location, best ping or the ability to set favourites.


# New Features!

  - Save favourites by adding **--save [name]** to the end of your command
  - Load a previously saved favourite by using **vanish -f [name]** to quick-connect


You can also:
  - Connect to a random server in a specified country by using **vanish -c XX** and the two letter ISO 3166 country code.
  - Connect to an activity specific VPN server by using **vanish -t [TOR|P2P|DEDI|VPN2]** (see below for details)
  - View your saved bookmarks by using **vanish -f** without a favourite specified

NordVPN is a popular VPN option which has an easiy to use client for Windows and MacOS, we wanted to create an easy to use command line option for linux users which can get you up and running with as simple as one word **vanish -r** which will connect you to a random option out of the 100s of worldwide servers.

> Historically, privacy was almost implicit, because it was hard to find and gather information.
> But in the digital world, whether it's digital cameras or satellites or just what you click on,
> we need to have more explicit rules - not just for governments but for private companies.
> **Bill Gates**


### Installation

Dillinger requires [OpenVPN](https://openvpn.com/) v4+ to run.

Install the dependencies and joka-vanishr, run as ($) either as root or with sudo.

```sh
$ cd /tmp
$ wget https://github.com/josh-tf/joka-vanish/joka-vanish-latest.deb
$ somecommand joka-vanish.latest.deb
```


### Main Commands

**Vanish** is easy to use and has a range of options for connecting to a VPN, these options are below.

| Command | Feature |
| ------ | ------ |
| vanish | View your current connection details |
| vanish -r | Connect to a random server|
| vanish -c [Country] | Connect to a random server in a specific country (ISO 3166 country code) |
| vanish -t [type] | Connect to a specific type of VPN, see options below. |
| vanish [opts] --save [name] | Save the connection options as favourite |
| vanish -f [name] | Connect to a previously saved favourite |
| vanish -help | View help information |

### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantanously see your updates!


### Todos

 - Write MOAR Tests
 - Add Night Mode

License
----

TBC

