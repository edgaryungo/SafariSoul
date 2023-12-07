<script>
	import {CulturalAttraction} from '../store';
    import { onMount } from 'svelte';
	
	onMount(async function () {
		const endpoint = 'http://0.0.0.0/api/cultural_attractions/'
		const response = await fetch(endpoint)
		const data = await response.json()
		// console.log(data)
		CulturalAttraction.set(data)
		})
</script>
<!-- class="flex flex-col lg:justify-center text-center lg:text-left gap-6 md:gap-8 lg:gap-10" -->

<main class="flex flex-col flex-1 p-4">
	<section id="Destination" class="py-20 lg:py-32 flex flex-col gap-24">
		<div class="grid grid-cols-1 lg:grid-cols-3 gap-12 lg:gap-10" data-sveltekit-prefetch>
			{#each $CulturalAttraction as culture}
				<div class="p-4 sm:p-6 md:p-8 flex flex-col gap-4 rounded-lg border border-solid border-violet-700 text-center group cursor-pointer hover:border-violet-400 duration-200">
					
					<img src="{culture.image}" alt="">
					<p class="text-base sm:text-lg md:text-xl">
						{culture.title}
						
					</p>
					
				</div>
			{/each}
		</div>
		
		
		
	</section>


</main>
