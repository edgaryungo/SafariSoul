<script>
    import {Destination} from '../../../store';
    export let data;
    const {destination} = data;
    Destination.set(destination)
</script>
<div class="container mx-auto h-screen">
    <div class="flex flex-col md:flex-row w-full md:w-1/2 h-1/2 p-4 object-cover gap-4 rounded-lg border border-solid border-violet-700 text-center group cursor-pointer hover:border-violet-400 duration-200">
      <img src="{$Destination.image}" alt="" class="w-full h-full object-cover" />
    </div>
    
    <div class="flex flex-col md:flex-row p-4 md:m-4 gap-4 rounded-lg  text-center group cursor-pointer hover:border-violet-400 duration-200">
      <div class="flex flex-col w-full md:w-1/2 p-4 gap-4 ">
        <h2 class="text-2xl font-bold">{destination.title}</h2>
        <p class="text-gray-500">{destination.description}</p>
        <p class="text-sm text-gray-400">Cultural Attraction: {destination.cultural_attraction}</p>
      </div>
      
      <div class="flex flex-col w-full md:w-1/2 p-4  gap-4 rounded-lg  text-center group cursor-pointer hover:border-violet-400 duration-200">
        <form>
          
          <button type="submit" class="blueShadow relative overflow-hidden px-5 py-2 group rounded-full bg-white text-slate-950 p-3 mt-4 items-center justify-center">
            <div
				class="absolute top-0 right-full w-full h-full bg-violet-400 opacity-20 group-hover:translate-x-full z-0 duration-200"
			/>
			<h4 class="relative z-9">Book Now</h4>
          </button>
        </form>
      </div>
    </div>
  </div>
  