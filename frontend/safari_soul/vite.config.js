import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {port:3000},
	build: {
		outDir: 'build', // Specify the output directory
	  },
});
