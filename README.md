# Acuiti-Hiring-Hack

**Note:** This is a skeleton repository, which should be [cloned] and used by participants of Acuiti Hiring Hack.

# Reverse engineering video codecs

## Objective
> There're three levels comprising unique difficulty.
> Study/Analyse input files and write a code to convert them into common h264/mp4 format.

## Resources / Tools
- ffmpeg, gstreamer, FormatFactory, CodecPack, gstring
- any hex editor (helps learn video encoding)
- gcc, g++, java or any of your favourite programming language to work with tools
- use any frameworks, 3rd party tools as long as it serves the objective of converting file.
- [bitbucket] and [git] tutorial to **create repository** and **push** the code :)


### Explaination
 Each level has various encoded files, and some may also have player with it.
 
* ### **Level - 1**
  * [VOB]
    * Points: **2** | Size: **21M**
    * This Level is really an exercise in knocking up a bit of code/tools that does the conversion of a known well documented format and does not require any real detective/decoding work.
    
  * [IVA]
    * Points: **2** | Size: **124M**
    * Chunk of files saperated by DD.MM.YYYY
    * Convert multitude of short ~1 minute .IVA files in a deeply nested "DD-MM-YYYY -> with sequential sub directories" structure into a single MP4/H.264 file!  

* ### **Level - 2**
  * [ARC]
    * Points: **4** | Size: **153M**
    * Might contain multiple feeds
  * [H264]
    * Points: **4** | Size: **811M**
    * To download inputfile: [H264.zip]
    * Contains executable **player.exe** which can play given **.h264**
    * 4-feed video
* ### **Level - 3**
  * [264]
    * Points: **6** | Size: **27M**
    * Contains executable **ProcessViewerPro.exe** which can play given **.264**
  * [PSF]
    * Points: **6** | Size: **132M**
    * Contains executable **Player_Launcher.exe** which can play given **.psf**
  * [EXE]
    * Points: **6** | Size: **136M**
    * To download inputfile: [Application.zip]
    * Self executable video with in-built player


## Deliverables
- Share repository url containing source code and the output video
- add instructions and technical documentation explaining how decoding was carried out
- If you feel that you want to use git to manage source code and for big files you may use Vimeo/Youtube to host output and link it in README.md inside respective output folder.
- Bitbucket can hold 1GB+ (max 2GB) on single repository, keep it public.


# Rules
> To be considered for the score associated with respective extension, you should provide source code + output video (h264/mp4) as deliverables.

> Source code, tools, and/or detailed description on decoding respective video extension should be provided through repository link (bitbucket supports +1.5G repository size).

> if you face difficulty pushing video on repository, feel free to upload video on (YouTube, Vimeo) and link it.



**Keep Reversing, Hell Yeah!**

   [IVA]: <https://bitbucket.org/pipaliya/acuiti-hiring-hack/src/31a168aacef3e6896386372065b24b7f92fbf7ba/Level-1/IVA/?at=master>
   [VOB]: <https://bitbucket.org/pipaliya/acuiti-hiring-hack/src/31a168aacef3e6896386372065b24b7f92fbf7ba/Level-1/VOB/?at=master>
   [ARC]: <https://bitbucket.org/pipaliya/acuiti-hiring-hack/src/31a168aacef3e6896386372065b24b7f92fbf7ba/Level-2/ARC/?at=master>
   [H264]: <https://bitbucket.org/pipaliya/acuiti-hiring-hack/src/31a168aacef3e6896386372065b24b7f92fbf7ba/Level-2/H264/?at=master>
   [264]: <https://bitbucket.org/pipaliya/acuiti-hiring-hack/src/31a168aacef3e6896386372065b24b7f92fbf7ba/Level-3/264/?at=master>
   [PSF]: <https://bitbucket.org/pipaliya/acuiti-hiring-hack/src/31a168aacef3e6896386372065b24b7f92fbf7ba/Level-3/PSF/?at=master>
   [EXE]: <https://bitbucket.org/pipaliya/acuiti-hiring-hack/src/31a168aacef3e6896386372065b24b7f92fbf7ba/Level-3/EXE/?at=master>
   [H264.zip]: <http://mirrors.hackerearth.0x10.info/seequestor/level-2/h264>
   [Application.zip]: <http://mirrors.hackerearth.0x10.info/seequestor/level-3/exe/Application.zip>
   [bitbucket]: <https://confluence.atlassian.com/bitbucket/bitbucket-tutorials-teams-in-space-training-ground-755338051.html>
   [git]: <https://confluence.atlassian.com/bitbucket/tutorial-learn-git-with-bitbucket-cloud-759857287.html>
   [cloned]: <https://bitbucket.org/pipaliya/acuiti-hiring-hack/src/?at=master#clone>

