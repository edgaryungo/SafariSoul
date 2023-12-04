import {writable} from 'svelte/store'

export const CulturalAttraction = writable([])
export const Destinations = writable([])
export const Packages = writable([])
export const Benefits = writable([
    {
        name: 'Tours & Travel',
        description: 'We offer a number of destinations with financially manageable packages '
    },
    {   name: 'Booking',
        description: 'You can book a destination from your bed of roses' 
    },
    {   name: 'Cultural Festivals',
        description: 'Some of the cultural interests..'
    }
])