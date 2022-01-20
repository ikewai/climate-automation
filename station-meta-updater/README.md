## Station Meta Updater

This container issues an asynchronous file transfer command to the Ike Wai gateway, to pull the latest version of the Climate Station Metadata file.

It may be run as a standalone docker container or on Abaco. It is designed to run on Abaco.

Inputs:
* Ike Wai Gateway Authentication Token
The token is input in the form of the `$IKEWAI_TOKEN` environment variable.
In Abaco it is brought in by means of the `default_environment` property when registering the actor.

Outputs:
* `importData` POST to Ike Wai Gateway, 1 file (approx. 100 MB)