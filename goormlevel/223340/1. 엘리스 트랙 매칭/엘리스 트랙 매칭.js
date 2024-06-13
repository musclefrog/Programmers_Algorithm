const solution = (N, info, self) => {
	info = info.split(" ");
	console.log(info.filter(x => x === self).length);
}

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

let count = 0;
let N = null;
let info = null;
let self = '';

rl.on("line", (line) => {
	if (!N) {
		N = +line;
	} else if (!info) {
		info = line;
	} else {
		self = line;
		count += 1;
	}
	if (count === 1) {
		rl.close();
	}
}).on('close', () => {
	solution(N, info, self);
	process.exit();
})