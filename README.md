## DifyGram

_the simplest way to run dify workflow in telegram_

## To run locally / develop:

1. copy `.env.example` to `.env` and fill the required fields (get bot token from botfather, and dify api from your dify workflow)
2. create a virtual environment `python3 -m venv venv`
3. activate the virtual environment `source venv/bin/activate`
4. install the dependencies `pip install -r requirements.txt`
5. run the server `python -m src.bot`
6. go to telegram and start the bot

## To deploy to digitalocean app platform:

**Note: Following these steps may result in charges for the use of DigitalOcean services.**

### Requirements

* You need a DigitalOcean account. If you don't already have one, you can sign up at https://cloud.digitalocean.com/registrations/new.

### Deploying the App

Click this button to deploy the app to the DigitalOcean App Platform. If you are not logged in, you will be prompted to log in with your DigitalOcean account.

[![Deploy to DigitalOcean](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/GeorgeStrakhov/DifyGram/tree/main)

Using this button disables the ability to automatically re-deploy your app when pushing to a branch or tag in your repository as you are using this repo directly.

If you want to automatically re-deploy your app, [fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) the GitHub repository to your account so that you have a copy of it stored to the cloud. Click the **Fork** button in the GitHub repository and follow the on-screen instructions.

After forking the repo, you should now be viewing this README in your own GitHub org (e.g. `https://github.com/<your-org>/DifyGram`). To deploy the new repo, visit https://cloud.digitalocean.com/apps and click **Create App**. Then, click **GitHub**, select the repository you created and select the `main` branch. App Platform will inspect the code, automatically detect the kind of component to create, and use the correct buildpack to create and deploy a container.

### Deleting the App

When you no longer need this sample application running live, you can delete it by following these steps:
1. Visit the Apps control panel at https://cloud.digitalocean.com/apps.
2. Navigate to the sample app.
3. In the **Settings** tab, click **Destroy**.

**Note: If you do not delete your app, charges for using DigitalOcean services will continue to accrue.**
