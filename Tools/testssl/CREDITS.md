
##### Credits also to

* David Cooper
  * Detection + output of multiple certificates
  * several cleanups of server certificate related stuff
  * fixing the file outputs
  * several further fixes
  * improved parsing of TLS ServerHello messages
  * speed improvements when testing all ciphers
  * extensive CN <--> hostname check
  * seperate check for curves

* Frank Breedijk
  * Detection of insecure redirects
  * JSON and CSV output
  * CA pinning
  * Client simulations
  * CI integration, test cases for it

* Peter Mosmans
  * started way better cmd line parsing
  * cleanups, fixes
  * openssl sources support with the "missing" features

* John Newbigin
  * Proxy support (sockets and openssl)

* Jonathan Roach
  * TLS_FALLBACK_SCSV checks

* Mark Felder
  * lots of cleanups
  * Shellcheck static analysis

- Christoph Badura
  * NetBSD fixes

* Jean Marsault
  * client auth: ideas, code snipplets

* Maciej Grela
   * colorless handling

* Olivier Paroz
   * conversion xxd --> hexdump stuff

* @typingArtist
   * improved BEAST detection

* @f-s
  * ARM binary support

* Jeroen Wiert Pluimers
   * Darwin binaries support

* Julien Vehent
  * supplied 1st Darwin binary

* Rechi
  * initial MX stuff
  * fixes

* Laine Gholson
  * avahi/mDNS support
  * HTTP2/ALPN
  * bugfixes
  * former ARM binary support
* Дилян Палаузов
  * bug fix for 3des report
  * reported a tricky STARTTLS bug

* Viktor Szépe
  * color function maker

* Thomas Martens
   * colorblind
   * no-rfc mapping

* Jonathon Rossi
   * fix for bash3 (Darwin)
   * and other Darwin fixes

* @nvsofts (NV)
  * LibreSSL patch for GOST

* Markus Manzke:
  * Fix for HSTS + subdomains
  * LibreSSL patch

* Dmitri S
  * inspiration & help for Darwin port

* Bug reports:
   * Viktor Szépe, Olivier Paroz, Jan H. Terstegge, Lorenz Adena, Jonathon Rossi, Stefan Stidl, Frank Breedijk

##### Last but not least:

* OpenSSL team for providing openssl.

* Ivan Ristic/Qualys for the liberal license of the API which made it possible to use the client data

* my family for supporting me doing this work

