# Twitter CLI

[![GitHub license](https://img.shields.io/github/license/shortthirdman/twitter-cli)](https://github.com/shortthirdman/twitter-cli/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/shortthirdman/twitter-cli)](https://github.com/shortthirdman/twitter-cli/issues)

A command-line interface utility for doing all things on the command shell/prompt - tweeting, reply to tweets, direct messaging.

## Getting Started

If you haven't already, the first thing to do is apply for a [developer account](https://developer.twitter.com/en/apply-for-access) to access Twitter APIs:
	`https://developer.twitter.com/en/apply-for-access`

After you have that access you can create a Twitter app and generate a `consumer_key`, `consumer_secret`, `access_token` and `access_token_secret`.

When you have your consumer key and its secret you authorize your Twitter account to make API requests with that consumer key and secret.

Make sure you have the environment variables in the system according to your operating system.

* For Windows using PowerShell

```powershell
[Environment]::SetEnvironmentVariable("CONSUMER_KEY", $consumerKey, "Machine")
[Environment]::SetEnvironmentVariable("CONSUMER_SECRET", $consumerSecretKey, "Machine")
[Environment]::SetEnvironmentVariable("ACCESS_TOKEN", $accessToken, "Machine")
[Environment]::SetEnvironmentVariable("ACCESS_TOKEN_SECRET", $accessTokenSecret, "Machine")
[Environment]::SetEnvironmentVariable("TWITTER_USERNAME", $userName, "Machine")
```

* For UNIX/Linux

```shell
export CONSUMER_KEY=consumerKey
export CONSUMER_SECRET=consumerSecretKey
export ACCESS_TOKEN=accessToken
export ACCESS_TOKEN_SECRET=accessTokenSecret
export TWITTER_USERNAME=userName
```

* For MacOS

```shell
```


## Installing

* For Node.js:
	`npm install -g twitter-cli`

* For Python:
	`pip install --user twitter-cli`
