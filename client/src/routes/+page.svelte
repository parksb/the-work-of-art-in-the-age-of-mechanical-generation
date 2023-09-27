<script>
  import { onMount } from 'svelte';

  onMount(() => {
    const audio = new Audio('/sfx.mp3');
    audio.loop = true;
    audio.play();

    const synth = window.speechSynthesis;
    const greeting = 'Hello, welcome to an exhibition that explores art in a whole new dimension. Here, we delve into the fascinating world of Artificial Intelligence and its role in creating artwork. We have two AI models. The first model is the one that speaks about the artwork it intends to create. The second model is the one that listens to the description and translates it into an actual visual piece. These two models work closely in collaboration to continuously produce artworks. We are moving beyond an era of mechanical replication to an era of mechanical generation.';
    const utterance = new SpeechSynthesisUtterance(greeting);
    utterance.rate = 0.9;
    synth.speak(utterance);
  });
</script>

<svelte:head>
  <title>The Work of Art in the Age of Mechanical Generation</title>
</svelte:head>

<div class="root">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Art-portrait-collage_2.jpg/600px-Art-portrait-collage_2.jpg" />
  <div class="label">
    <p class="title">No. 01</p>
    <p class="material">2023, Oil on canvas</p>
    <p class="size">20 × 20 cm</p>
  </div>
</div>

<style>
  .root, .label {
    display: flex;
  }

  .root {
    justify-content: center;
  }

  .label {
    flex-direction: column;
    justify-content: flex-end;
    margin-left: 20px;
    color: white;
    font-family: serif;

    & > p {
      margin: 0;
    }

    & > p.title {
      font-size: 1.3rem;
      font-weight: bold;
    }
  }
</style>
