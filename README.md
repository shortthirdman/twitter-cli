# Twitter CLI

[![GitHub license](https://img.shields.io/github/license/shortthirdman/twitter-cli)](https://github.com/shortthirdman/twitter-cli/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/shortthirdman/twitter-cli)](https://github.com/shortthirdman/twitter-cli/issues)
[![GitHub package.json keywords](https://img.shields.io/github/package-json/keywords/shortthirdman/twitter-cli)](https://github.com/shortthirdman/twitter-cli)
[![GitHub package.json version](https://img.shields.io/github/package-json/version/shortthirdman/twitter-cli)](https://github.com/shortthirdman/twitter-cli)

![GitHub last commit](https://img.shields.io/github/last-commit/shortthirdman/twitter-cli)
![Weekly GitHub commit activity](https://img.shields.io/github/commit-activity/w/shortthirdman/twitter-cli?label=Weekly)
![Monthly GitHub commit activity](https://img.shields.io/github/commit-activity/m/shortthirdman/twitter-cli?label=Monthly)
![Yearly GitHub commit activity](https://img.shields.io/github/commit-activity/y/shortthirdman/twitter-cli?label=Yearly)

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

## Help and Resources

* [geduldig/TwitterAPI: Minimal python wrapper for Twitter's REST and Streaming APIs](https://github.com/geduldig/TwitterAPI)
* [draftbit/twitter-lite: A tiny, full-featured, flexible client / server library for the Twitter API](https://github.com/draftbit/twitter-lite)
* [HunterLarco/twitter-v2: An asynchronous client library for the Twitter REST and Streaming API's](https://github.com/HunterLarco/twitter-v2)
* [Publishing Node.js packages](https://docs.github.com/en/actions/guides/publishing-nodejs-packages)
