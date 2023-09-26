<svelte:head>
  <title>The Work of Art in the Age of Mechanical Generation</title>
</svelte:head>

<div class="root">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Art-portrait-collage_2.jpg/600px-Art-portrait-collage_2.jpg" />
  <div class="label">
    <p class="title">No. 01</p>
    <p class="material">2023, Oil on canvas</p>
    <p class="size">13cm x 13cm</p>
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

    & > p {
      margin: 0;
    }

    & > p.title {
      font-size: 1.3rem;
      font-weight: bold;
    }
  }
</style>
