<script>
  import { onMount } from 'svelte';

  $: version = 0;

  const apiUrl = import.meta.env.VITE_API_URL;

  onMount(() => {
    const audio = new Audio('/morse-1.mp3');
    audio.loop = true;
    audio.play();

    setInterval(async () => {
      const image_ready = (await (await fetch(`${apiUrl}/image_ready?x=${version}`)).text()) == 'true';
      if (image_ready) {
        version += 1;
      }
    }, 500);
  });
</script>

<svelte:head>
  <title>The Work of Art in the Age of Mechanical Generation</title>
</svelte:head>

<div class="root">
  <img src={`${apiUrl}/image?p=${version}`} alt="A generated artwork" />
  <small>No. {version + 1} (2023)</small>
</div>

<style>
  .root {
    display: flex;
    flex-direction: column;
  }

  img {
    display: block;
    width: 100%;
  }

  small {
    display: block;
    color: white;
    margin-top: 5px;
    text-align: right;
  }
</style>
