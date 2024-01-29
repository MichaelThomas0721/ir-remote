<script>
	export let name;
	let pendings = [];

	let xhr = new XMLHttpRequest();

	xhr.onload = function () {
		// output.textContent = xhr.responseText;
		pendings = JSON.parse(xhr.responseText);
		setTimeout(() => SendXHR(), 1000);
	};

	function SendXHR() {
		xhr.open("GET", "stream");
		xhr.send();
	}

	function StartRecording() {
		SendXHR();
		let tempXhr = new XMLHttpRequest();
		tempXhr.onload = function () {
			console.log(tempXhr.responseText);
		};
		tempXhr.open("GET", "{{ url_for(`start_recording`)}}");
		tempXhr.send();
	}

	function ViewPendings() {
		SendXHR();
	}
</script>

<main>
	<h1 class="bg-blue-500">Hello adfadf{name}!</h1>
	<p>
		Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn
		how to build Svelte apps.
	</p>
	<button on:click={StartRecording}>Start Recordign</button>
	<button on:click={ViewPendings}>View Pendings</button>
	<h3>Pendings:</h3>
	<div id="pendingCont">
	{#each pendings as pending}
	<p>{pending}</p>
	{/each}
	</div>
</main>

<style lang="postcss" global>
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	#pendingCont {
		display: flex;
		flex-direction: column;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
