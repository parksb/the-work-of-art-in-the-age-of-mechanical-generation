<script lang="ts">
  import { onMount } from 'svelte';

  $: version = 0
  $: prompt = "Hello. From now on, I will freely talk about things I imagine. Please draw what I'm saying so that it can be seen with the eyes.";
  $: indicator = "□";

  const apiUrl = import.meta.env.VITE_API_URL;

  const materials = ["A landscape of ", "The people who ", "A building that ", "A still life depicting ", "A cityscape of ", "An oil painting depicting ", "An ink wash painting depicting ", "An abstraction of "];

  onMount(async () => {
    const audio = new Audio('/morse-2.mp3');
    audio.loop = true;
    audio.play();

    setTimeout(() => {}, 5000);

    setInterval(async () => {
      if (indicator == "□") {
        indicator = "■";
      } else {
        indicator = "□";
      }

		  const image_ready = (await (await fetch(`${apiUrl}/image_ready?x=${version}`)).text()) == 'true';

      if (image_ready) {
        version += 1;

        const material = encodeURI(materials[Math.floor(Math.random() * materials.length)]);
        const raw_prompt = (await (await fetch(`${apiUrl}/prompt?x=${material}`)).text())
        const refined_prompt = raw_prompt.replace(/^"|"$/g, "").replace(/\\n/g, "").replace(/,$/g, "");

        await fetch(`${apiUrl}/new?prompt=${refined_prompt}`);
        prompt = refined_prompt
      }
    }, 500);
  });
</script>

<svelte:head>
  <title>The Work of Art in the Age of Mechanical Generation</title>
</svelte:head>

<div class="root">
  <div class="label">
    <p>{prompt} {indicator}</p>
  </div>
</div>

<style>
  .root {
    max-width: 100%;
    padding: 10%;
  }

  p {
    color: white;
    font-size: 28px;
  }
</style>
