![Forks][forks-shield]
![Stargazers][stars-shield]
![Issues][issues-shield]

<br />
<p align="center">
  <a href="https://github.com/roshanlam/ReadMeTemplate/">
    <img src="./logo.png" alt="Logo" width="200" height="150">
  </a>

  <h3 align="center">SpotMusicGen (Master Branch) </h3>

  <p align="center">

  <br />
   <a href="https://github.com/roshanlam/SpotMusicGen/issues">Report Bug</a>
    ·
   <a href="https://github.com/roshanlam/SpotMusicGen/issues">Request Feature</a>
    ·
   <a href="https://github.com/roshanlam/SpotMusicGen/pulls">Send a Pull Request</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Set Up](#setup)
* [Contributing](#contributing)
* [Contact](#contact)
* [To Do](#todo)
* [TroubleShooting](#Trouble-shooting)


<!-- ABOUT THE PROJECT -->
## About The Project

Hasn't there been a time when you listened to song but didn't want to do the work to put that song on your spotify playlist. Cause that happened to me and I wanted to slove it and this is my solution. What SpotMusicGen does is it takes all of the liked songs from your youtube channel and generates a spotify playlist.

## SetUp

1. Install All Dependencies
   `pip3 install -r requirements.txt`
   
2. Get your Credentials and save it in `.env`

https://console.cloud.google.com/apis/credentials

https://developer.spotify.com/dashboard/applications


3. Add redirect uri in the edit settings for spotify

4. Run the File
    `python3 main.py`
   
5. Enter the playlist id and the name you want it to be on spotify


## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **extremely appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Contact

Email - roshanlamichhanenepali@gmail.com

## ToDo
* Tests
* Add Error Handling
* Add a feature for Soundcloud
* Add a Voice Assistant that will play/stop/repeat music for you while you are coding

[issues-shield]:https://img.shields.io/github/issues/roshanlam/SpotMusicGen?style=for-the-badge
[stars-shield]: https://img.shields.io/github/stars/roshanlam/SpotMusicGen?style=for-the-badge
[forks-shield]: https://img.shields.io/github/forks/roshanlam/SpotMusicGen?style=for-the-badge
