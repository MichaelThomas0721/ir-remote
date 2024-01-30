<script>
  import { Button } from '@svelteuidev/core';
  import Pending from './components/Pending.svelte';
  let pendings = [];

  let selectedPending = 0;

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

  function ClickPending(id) {
    selectedPending = id;
    document.getElementById('pendingModal').showModal();
  }
</script>

<main class="flex flex-col items-center justify-center w-fit">
  <h1 class="text-3xl font-bold">IR Remote</h1>
  <div class="flex flex-row w-fit gap-3 items-center">
    <button class="btn btn-primary" on:click="{StartRecording}"
      >Start Recording</button
    >
    <button class="btn btn-secondary" on:click="{ViewPendings}"
      >View Pendings</button
    >
  </div>

  <h3>Pendings:</h3>
  <div id="pendingCont" class="gap-3 flex flex-col items-center">
    {#each pendings as pending}
      <Pending pendingData="{pending}" ClickPending="{ClickPending}" />
    {/each}
  </div>

  <dialog id="pendingModal" class="modal">
    <div class="modal-box">
      <h3 class="font-bold text-lg">Name Pending IR Signal</h3>
      <input
        type="text"
        placeholder="{pendings?.[selectedPending]?.[2]}"
        class="input input-bordered input-secondary w-full max-w-xs"
      />
    </div>
    <form method="dialog" class="modal-backdrop">
      <button>close</button>
    </form>
  </dialog>
</main>

<style lang="css">
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
