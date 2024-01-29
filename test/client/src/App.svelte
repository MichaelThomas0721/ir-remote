<script>
  import { Button } from '@svelteuidev/core';
  let pendings = [];

  let xhr = new XMLHttpRequest();

  xhr.onload = function () {
    // output.textContent = xhr.responseText;
    pendings = JSON.parse(xhr.responseText);
    setTimeout(() => SendXHR(), 1000);
  };

  function SendXHR() {
    xhr.open('GET', 'stream');
    xhr.send();
  }

  function StartRecording() {
    SendXHR();
    let tempXhr = new XMLHttpRequest();
    tempXhr.onload = function () {
      console.log(tempXhr.responseText);
    };
    tempXhr.open('GET', 'start_recording');
    tempXhr.send();
  }

  function ViewPendings() {
    SendXHR();
  }
</script>

<main class="flex flex-col items-center">
  <h1 class="text-3xl font-bold">IR Remote</h1>
  <div class="flex flex-row gap-3 items-center align-middle">
  <button class="btn btn-primary" on:click={StartRecording}>Start Recording</button>
  <button class="btn btn-secondary" on:click={ViewPendings}>View Pendings</button>
  </div>
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
</style>
