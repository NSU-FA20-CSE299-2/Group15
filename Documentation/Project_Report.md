# Project Report

IPTV:
We started our project, IPTV with a purpose of offering better and easy to access tv streaming site, where we all can watch tv and enjoy ourselves! Through out the semester, we faced some difficulties completing the project.

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
|Admin panel|Functions properly.|..|
|Dockerization| It's now running on python package manager|Once project finishes it'll be dockerized.|

## Frontend
We used..
- HTML
- CSS
- JavaScript

For framework we used..
- Bootstrap 5.0
- Material design 2.0

## Backend
We used..
- NGINX server - for video content delivery
- RTMP Nginx module - for ingesting rtmp video and convert it to HLS stream
- Django-(3.1) - for backend
- Django countries-(7.0) - for adding all countries in the database


## Database
As we are operating this project on small scale, so we used SQLite. When we will be operating it on bigger scale we will switch to MariaDB/MongoDB or firebase.

## Additional technologies
We didn't use Allauth. We used Django Contrib Authentication module for Login and Logout.
For regsitration we used Django contrib auth forms.
Also we used Django contrib auth decorator for login requirement or restricting access to all anonymous users