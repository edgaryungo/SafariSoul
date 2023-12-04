<script>
    export let data;
    const {destination} = data;
</script>

<h1>
    <!-- slug is -- {data.destination.slug} -->
    {destination.title}
</h1>
<!-- <img src="{data.destination.image}" alt=""> -->