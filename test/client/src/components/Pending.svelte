<script>
  export let pendingData;
  export let ClickPending;
  console.log(pendingData);
</script>

<button class="btn btn-outline btn-primary" on:click={() => ClickPending(pendingData[0])}>
  {pendingData[0]} |
  {pendingData[2]}
</button>
