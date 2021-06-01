# twitter-cli

A command-line interface utility for doing all things on the command shell/prompt - tweeting, reply to tweets, direct messaging.

## Getting Started

If you haven't already, the first thing to do is apply for a [developer account](https://developer.twitter.com/en/apply-for-access) to access Twitter APIs:
	`https://developer.twitter.com/en/apply-for-access`

After you have that access you can create a Twitter app and generate a `consumer_key`, `consumer_secret`, `access_token` and `access_token_secret`.

When you have your consumer key and its secret you authorize your Twitter account to make API requests with that consumer key and secret.

Make sure you have the environment variables in the system according to your operating system.

* For Windows using PowerShell

```powershell
[Environment]::SetEnvironmentVariable("TW_CONSUMER_KEY", $consumerKey, "Machine")
[Environment]::SetEnvironmentVariable("TW_CONSUMER_SECRET", $consumerSecretKey, "Machine")
[Environment]::SetEnvironmentVariable("TW_ACCESS_TOKEN", $accessToken, "Machine")
[Environment]::SetEnvironmentVariable("TW_ACCESS_TOKEN_SECRET", $accessTokenSecret, "Machine")
[Environment]::SetEnvironmentVariable("TW_USERNAME", $userName, "Machine")
```

* For UNIX/Linux
```shell
```

* For MacOS
```shell
```


## Installing

* For Node.js:
	`npm install -g twitter-cli`

* For Python:
	`pip install --user twitter-cli`
