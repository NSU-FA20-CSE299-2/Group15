# Project Report

IPTV:
We started our project,IpTv with a purpose of offering better and easy to access tv streaming site, where we all can watch tv and enjoy ourselves! Through out the semester, we faced some difficulties completing the project.

## Progress

|Features|Working features|Under-developed features|
|-|-|-|
|Signup/Register|It's working via email address.| Login with phone number.|
|High Quality Video Streaming | Supports upto 4k |..| 
|Computer and smartphone supportibility| It supports. We also made it responsive.|.. |
|Smart Tv for streaming IPTV|JScript supported players can stream.|M3U playlist for smart tv.|
|Payment gateway|..|Online payment.|
|Customizable profile|..|Need more time.|
|2 step verification|..|Need more time.|
|Channels|..|Channel search by name,genre etc|
|||Favourite channel list|
|||Channel auto suggestion|
|Admin panel|Funstions properly.|..|
|Dockerization| It's now running on python.|Once project finishes it'll be dockerized.|

## Frontend
We used..
- HTML
- CSS
- JavaScript

We also used ..
- Bootstrap(5)
- Material design(MD2)

## Backend
We used..
- NGINX we server
- RTMP Nginx module
- Django-(3.1)
- Django countries-(7.0)

Django countries(7.0) helps us findiing the country names for the channels.

## Database
As we are operating this project on small scale, so we used SQLite. When we will be operating it on bigscale then we will switch to MariaDB/MongoDB.

## Additional technologies
We didn't use Allauth. We used Django Contrib Authentication module for Login and Logout.