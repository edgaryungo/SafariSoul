<script>
	import Step from './Step.svelte';
	// import {CulturalAttraction} from '../store';
	// import {Destinations} from '../store';
	// import {Packages} from '../store';
	import { Benefits } from '../store';
	// import {onMount} from 'svelte';


	let steps = [
		{ name: 'Cultural Attractions', icon: 'fas fa-umbrella-beach', href:'culture'},
		{ name: 'Destinations', icon: 'fas fa-map-marked', href:'destinations' },
		{ name: 'Popular Destinations', icon: 'fa-diagram-project' }
	];

</script>

<main class="flex flex-col flex-1 p-4">
	<section id="Home" class="grid grid-cols-1 lg:grid-cols-2 gap-10 py-8 sm:py-14">
		<div class="flex flex-col lg:justify-center text-center lg:text-left gap-6 md:gap-8 lg:gap-10">
			<h2 class="font-semibold text-4xl sm:text-5xl md:text-6xl">
				Experience <span class="poppins text-violet-400">Nature</span>Culture<br /> with us
			</h2>
			<p class="text-base sm:text-lg md:text-xl">
				Let <span class="text-violet-400">us fulfill</span> your travel dreams
			</p>
			<a
				class="blueshadow mx-auto lg:mr-auto lg:ml-0 text-base sm:text-lg md:text-xl poppins relative overflow-hidden px-6 py-3 group rounded-full bg-white text-slate-950 cursor-pointer"
				href="/"
			>
				<div
					class="absolute top-0 right-full w-full h-full bg-violet-400 opacity-20 group-hover:translate-x-full z-0 duration-200"
				/>
				<h4 class="relative z-9">Get in touch &rarr;</h4>
			</a>
		</div>
		<div class="relative shadow-2xl grid place-items-center">
			<img src={'images/image.png'} alt="" class="object-cover z-[2] max-h-[100vh] max-w-[100vw]" />
		</div>
	</section>

	<section id="Destinations" class="py-20 lg:py-32 flex flex-col gap-24">
		<div class="flax flex-col gap-2 text-center">
			<h6 class="text-lg sm:text-xl md:text-2xl">A few combinations for you</h6>
			<h3 class="font-semibold text-3xl sm:text-4xl md:text-5xl">
				Curious to <span class="poppins text-violet-400">See</span> Them?
			</h3>
		</div>
		<a
			href="/"
			class="mx-auto px-4 py-2 rounded-md border border-solid border-white flex items-center gap-2 -mb-4 sm:-mb-0 -mt-10 hover:border-violet-700 duration-200"
		>
			<i class="fa-regular fa-circle-play"></i>
			<p>Watch the video</p>
		</a>
		<div class="grid grid-cols-1 lg:grid-cols-3 gap-12 lg:gap-10">
			<Step step={steps[0]}>Check out</Step>

			<Step step={steps[1]}>Dream Destinations</Step>

			<Step step={steps[2]}>Most liked Destinations</Step>
		</div>
	</section>
	<section
		id="About"
		class="py-20 pt-10 lg:pt-16 lg:py-32 flex flex-col gap-16 sm:gap-20 md:gap-24 relative"
	>
		<div
			class="flex flex-col gap-2 text-center relative before:absolute before:top-0 before:left-0 before:w-2/3 before:h-1.5 before:bg-violet-700 after:absolute after:bottom-0 after:right-0 after:w-2/3 after:h-1.5 after:bg-violet-700 py-4"
		>
			<h6 class="text-lg sm:text-xl md:text-2xl">Want to know more?</h6>
			<h3 class="font-semibold text-3xl sm:text-4xl md:text-5xl">
				A bit <span class="poppins text-violet-400">about</span> us.
			</h3>
		</div>
		<p class="mx-auto poppins font-semibold text-lg sm:text-xl md:text-2xl">We <span class="text-violet-400">Redefine</span> . . .</p>
		<div class="flex flex-col gap-20 w-full mx-auto max-w-[800px]">
			{#each $Benefits as benefit, index}
				<div class="flex gap-6 sm:gap-8">
					<p class="poppins text-4xl sm:text-5xl md:text-6xl text-slate-500 font-semibold">
						0{index + 1}
					</p>
					<div class="flex flex-col gap-6 sm:gap-8">
						<h3 class="text-2xl sm:text-3xl md:text-5xl">
							{benefit.name}
						</h3>
						<p>{benefit.description}</p>
					</div>
				</div>
			{/each}
		</div>
		<p class="mx-auto">So why not invest?</p>
	</section>
</main>

