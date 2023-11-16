<script lang="ts">
  import { onMount } from 'svelte';

  $: version = 0
  $: prompt = "Hello. From now on, I will freely talk about things I imagine. Please draw what I'm saying so that it can be seen with the eyes.";

  // function speak(text: string) {
  //   const synth = window.speechSynthesis;
  //   const utterance = new SpeechSynthesisUtterance(text);
  //   utterance.rate = 0.9;
  //   synth.speak(utterance);
  //
  //   return new Promise(resolve => {
  //     utterance.onend = resolve;
  //   });
  // }

  const apiUrl = import.meta.env.VITE_API_URL;

  const materials = ["A landscape", "The people", "A building", "A person", "A still life", "A cityscape", "An oil painting", "An ink wash painting", "An abstraction"];

  onMount(async () => {
    // await speak(prompt);

    const audio = new Audio('/morse.mp3');
    audio.loop = true;
    audio.play();

    setTimeout(() => {}, 5000);

    setInterval(async () => {
		  const image_ready = (await (await fetch(`${apiUrl}/image_ready?x=${version}`)).text()) == 'true';

      if (image_ready) {
        version += 1;

        const material = encodeURI(materials[Math.floor(Math.random() * materials.length)]);
        prompt = (await (await fetch(`${apiUrl}/prompt?x=${material}`)).text())
        prompt = prompt.substring(1, prompt.length - 1).replace(/,$/g, "").replace(/\n/g, "");

        fetch(`${apiUrl}/new?prompt=${prompt}`);

        // await speak(prompt);
      }
    }, 500);
  });
</script>

<svelte:head>
  <title>The Work of Art in the Age of Mechanical Generation</title>
</svelte:head>

<div class="root">
  <div class="label">
    <p>{prompt}</p>
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
