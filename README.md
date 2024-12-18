
# Arts Forum Web Application

## Overview

This project is an academic web application developed using the Django framework to create a community-driven platform for art enthusiasts. It provides a space for users to share artistic content, auction their creations, and participate in community events. The platform also emphasizes secure deployment and software quality using cloud-based DevOps practices.

AWS services like Elastic Beanstalk, S3, CodePipeline, and SonarCloud are integrated to ensure secure deployment, static code analysis, and continuous delivery. The project prioritizes usability, scalability, and adherence to security standards.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technologies and Dependencies](#technologies-and-dependencies)
6. [Deployment](#deployment)
7. [Contributors](#contributors)
8. [License](#license)

## Introduction

The Arts Forum application provides users with the ability to:
- Share their artistic creations with a like-minded community.
- Auction their art pieces via a bidding system.
- Organize and register for community events.

The project integrates AWS cloud services and includes a CI/CD pipeline with static and security code analysis to ensure high-quality and secure application delivery.

## Features

### User Roles
- **Admin**: Full access to application data and the ability to assign user roles.
- **Supervisor**: Moderates content, addresses user queries, and manages events.
- **Normal User**: Posts content, participates in auctions, and registers for events.

### Modules
1. **Content Posting**: Users can share artistic content and manage their posts.
2. **Bidding on Arts**: Auction system for buying and selling art pieces.
3. **Community Events**: Supervisors can create events, and users can register individually or as a group.

### Security and Analysis
- Static code analysis with Pylint.
- Security vulnerability analysis using SonarCloud.
- Secrets management for environment variables.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ashwinsabu/ArtsForum.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ArtsForum
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/MacOS
   venv\Scripts\activate      # For Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Apply migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

Access the application locally at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Technologies and Dependencies

- **Backend**: Django (Python Framework)
- **Frontend**: HTML, Bootstrap
- **Database**: SQLite
- **Cloud Services**: AWS (Elastic Beanstalk, S3, CodePipeline, CodeBuild)
- **Code Analysis**: Pylint, SonarCloud

## Deployment

The application is deployed using AWS Elastic Beanstalk with a CI/CD pipeline managed through AWS CodePipeline. This pipeline includes stages for:
1. Static code analysis with Pylint.
2. Security vulnerability checks using SonarCloud.
3. Automated deployment to Elastic Beanstalk.

## Contributors

- **Ashwin Sabu**
  - **Email**: [x23196505@student.ncirl.ie](mailto:x23196505@student.ncirl.ie)
  - **Institution**: National College of Ireland

## License

This project is for academic purposes and does not currently include a specific license.
