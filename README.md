# snapshotanalyzer

Demo project to manage AWS EC2 instance snapshots

## About

This demo project uses boto3 to manage
AWS EC2 instance snapshots.

## Configuring

shotan uses the configuration file created by the AWS cli e.g.,

'aws configure --profile shotan'

## Running
'pipenv run "python shotan/shotan.py <command> <--project=PROJECT>"'

*command* is instances, volumes, or snapshots
*subcommand* - depends on command
*project* is optional
