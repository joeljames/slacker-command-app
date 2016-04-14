Simple slack slash command app.

## Available Commands

| Command                          | Description                                                |
| -------------------------------- |:----------------------------------------------------------:|
| /user [username]                 | Gets the specified users email and phone from the profile  |



## Set up Docker Environment (Mac)
I use Mac for local development. Below are the instructions to set up
Docker on Mac

1. Install [Dinghy](https://github.com/codekitchen/dinghy)

2. Install [docker toolbox](https://www.docker.com/products/docker-toolbox)

3. Install [Virtual Box](https://www.virtualbox.org/wiki/Downloads)

4. Creat the docker-machine VM. Make sure to alocate enough resources to the VM.

    ``` bash
    $ dinghy create --disk=60000 --provider=virtualbox
    ```

5. Start the Docker VM and services

    ``` bash
    $ dinghy up
    ```

## Getting Started to Setup the App Locally

This app is set up to run within a Docker Container.
The tools and steps required to run this application is defined within the
`Dockerfile` which is present at the root of the project directory.
The app processes (web) are defined within `docker-compose-base.yml` and `docker-compose.yml`.

Below are the steps to build and get the container up and running.

A list of make commands are available for managing tasks. You can view the list by running `make help` command.

1. Generate the slack token [here](https://api.slack.com/web#authentication). Set this token in the `env.ini` file after completing step 2

2. Setup environment. Make sure to manually configure the required env variables in `env.ini` file after running the command below.

    ``` bash
    $ make copy_env
    ```

3. Build the image:

    ``` bash
    $ docker-compose build
    ```

4. Start the server:

    ``` bash
    $ docker-compose up
    ```

5. Check the server is up and running by hitting the url POST `http://slacker-command.docker/`.
