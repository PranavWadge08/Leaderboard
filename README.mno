<img src="https://tachyonbyte.s3.ap-south-1.amazonaws.com/static/assets/img/fullwhite.png" alt="TachyonByte" width="200"/>

[![CI/CD](https://github.com/TachyonByte/Leaderboard/actions/workflows/cicd.yml/badge.svg)](https://github.com/TachyonByte/Leaderboard/actions/workflows/cicd.yml)

# Leaderboard Project

Capture the Flag (CTF) competitions are exciting events where teams compete by solving security challenges. The Leaderboard project acts as the heart of a CTF, allowing organizers to manage challenges, track team scores in real-time, and provide transparency to participants. This project is designed for both CTF organizers and participants to enhance the competition experience.

## Features

- **Live Leaderboard Updates**: Witness scores change as teams solve challenges, fueling the competitive spirit!
- **Secure Authentication**: User accounts and session management ensure data integrity and prevent unauthorized access.
- **Streamlined Score Submission**: Submit scores effortlessly and enjoy a seamless verification process.
- **Intuitive Admin Panel**: Manage challenges, add teams, and customize the competition experience with ease.
- **Built-in Security Measures**: Rest assured; robust security features safeguard against cheating and ensure a level playing field.


## Technologies Used
- **Django**: A robust Python web framework for rapid development.
- **Django-Channels**: Enables real-time communication for dynamic leaderboard updates.
- **Redis**: High-performance data store for caching and real-time interactions.
- **Docker**: Simplifies deployment and ensures consistent environments.
- **Github Actions**: Automates testing and deployment for a streamlined workflow.
## Installation

You can easily run the Leaderboard project using Docker or Docker Compose. The project has been containerized and is available as an image on Docker Hub.

### Option 1: Using Docker

1. **Pull the Docker image:**

   ```bash
   docker pull tachyonbyte/leaderboard:latest
   ```

   Docker Hub link: [tachyonbyte/leaderboard](https://hub.docker.com/r/tachyonbyte/leaderboard)

2. **Run the container:**

   ```bash
   docker run -d -p 80:80 tachyonbyte/leaderboard:latest 
   ```

3. **Implement persistence with volume mount (optional):**

   To ensure data persistence, you can mount a volume for the SQLite database:

   ```bash
   docker run -d -p 80:80 --mount source=sqlite-db,target=/app/ctf/ tachyonbyte/leaderboard:latest
   ```

   This command mounts the local `sqlite-db` volume to the container’s `/app/ctf/` directory, where the database is stored.

4. **Access the leaderboard:**  
   Visit `http://localhost` in your browser. use email "admin@admin.com" and password "tulakaymahit"

---

### Option 2: Using Docker Compose

Follow these steps to set up the Leaderboard project using Docker Compose:

1. **Create a `docker-compose.yml` file:**

   ```yaml
   services:
      app:
         depends_on:
            - redis
         image: tachyonbyte/leaderboard:latest
         ports:
            - "80:80"
         volumes:
            - sqlite-db:/app/ctf/ctf/db.sqlite3

      redis:
         image: redis:alpine

   volumes:
      sqlite-db:
         driver: local
   ```

2. **Run the Docker Compose setup:**

   Navigate to the directory where the `docker-compose.yml` file is saved and run:

   ```bash
   docker-compose up -d
   ```

   This will pull the necessary Docker image, create the required containers, and run the application.

3. **Access the leaderboard:**  
   Visit [`http://localhost`](http://localhost) in your browser.

4. **Stop the application (when needed):**

   ```bash
   docker-compose down
   ```

This method simplifies running the application and managing dependencies through a single command.

## Usage

- Access the leaderboard and manage teams and challenges via the provided interface.
- Submit scores and track rankings in real-time.

## Credits
- [Tanmay More]([https://github.com/tanmay-more-dev]) - Implemented core functionality, designed the architecture
- [Purvesh Wakode]([https://github.com/purvesh0110]) - Implemented Github Actions
- [Abhijit More]([https://github.com/mabhi49]) - Containerised the project
- [Paresh Pawar]([https://github.com/pareshpawar]) - Planning and Management



## Contributing

Feel free to submit issues and pull requests to help improve the project.
