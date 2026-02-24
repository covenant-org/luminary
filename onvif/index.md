# Onvif

This is a reference roadmap for the inclusion of onvif functionality into the argus station proyect

## General roadmap

![roadmap](https://covenant-org.github.io/luminary/static/preview.webp)


### Step 1

For fast deploy and proof of concept the use of a not so optimal ready to use solution is the way to go
Options:
 - https://github.com/jimm98y/SharpOnvif
 - https://github.com/daniela-hase/onvif-server
 - https://github.com/mpromonet/v4l2onvif
 - https://github.com/Quedale/rpos
 - https://github.com/KoynovStas/onvif_srvd
 - https://github.com/roleoroleo/onvif_simple_server
 - https://github.com/hummatli/onvif-qt-server-client
 - https://github.com/As772309423/onvif-server-with-rtsp
 - https://github.com/Quedale/OnvifRtspLauncher

This options center around [Profile S](https://covenant-org.github.io/luminary/onvif/#profiles) and since the official testing tools are behind a pay wall this tools
could be use to test the implementation

 - https://github.com/Quedale/OnvifDeviceManager
 - https://github.com/jfsmig/onvif

### Step 2

After a short analysis and lack of experience with the onvif protocol I believe that the route for long term
support and custom features is to implement our own onvif server. For doing so, the first step is to create an
implementation for [Profile S](https://covenant-org.github.io/luminary/onvif/#profiles) and then add the discovery ([Reference implementation](https://github.com/KoynovStas/wsdd))
functionality. And finally the part with the least number of examples, the VOD or Replay features, [Profile G](https://covenant-org.github.io/luminary/onvif/#profiles)


### Step 3

After having a functional prototype the next step is to actually certify it agains onvif as we cannot announce
the compatibility with the protocol without being approved by them.

Before we can summit an application it is necessary to become "members", in order to do so we need to follow these
[instructions](https://www.onvif.org/wp-content/uploads/2017/02/instructions_for_obtaining_membership.pdf) and pay
a fee corresponding to the membership fee we desire to become.

The membership levels are listed [here](https://www.onvif.org/join-us/membership-levels/) but my recomendation is
level User, which allows to summit apps for verification at the lowest price.
The user membership cost $4,000 USD/year


## Profiles

Profiles are the way of onvif to differentiate the types of equipments in a system and to match capable clients with
equally capable devices. In other words, each profile as its use and the pair client-server must confirm with the same
profile to communicate in onvif terms

For the project I see only 2 relevant profiles:

 - Profile S: The most basic profile for streaming.
 - Profile G: The profile for playback and recording.

The list of all the profiles can be found [here](https://www.onvif.org/profiles/)


