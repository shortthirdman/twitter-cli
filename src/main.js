const axios = require('axios');
const fs = require('fs');
const path = require('path');
const chalk = require('chalk');
const boxen = require('boxen');
const yargs = require('yargs');
const twitter = require('twitter-text');

const { data } = await client.get('tweets', { ids: '1228393702244134912' });
console.log(data);

const options = yargs
 .usage('Usage: -n <name>')
 .option('n', { alias: 'name', describe: 'Your name', type: 'string', demandOption: true })
 .option('s', { alias: 'search', describe: 'Search term', type: 'string' })
 .argv;

const greet = function() {
	const boxenOptions = {
	 padding: 1,
	 margin: 1,
	 borderStyle: 'round',
	 borderColor: 'green',
	 backgroundColor: '#555555'
	};
	const greeting = `Hello, ${chalk.white.bold(options.name)}!`;
	const msgBox = boxen( greeting, boxenOptions );
	console.log(msgBox);
}
