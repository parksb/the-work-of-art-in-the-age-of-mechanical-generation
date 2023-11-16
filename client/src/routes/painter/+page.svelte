<script>
  import { onMount } from 'svelte';

  $: version = 0;

  const apiUrl = import.meta.env.VITE_API_URL;

  onMount(() => {
    const audio = new Audio('/morse.mp3');
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
</div>

<style>
  .root {
    display: flex;
  }

  img {
    width: 100%;
    height: 100%;
  }
</style>
