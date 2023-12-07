export async function load({fetch, params}){
    

    const fetchDest = async (slug) => {
        const endpoint = `http://0.0.0.0:8000/api/destinations/${slug}`
        const result = await fetch(endpoint)
        const data = await result.json()
        return data
    }
    return {
       destination: fetchDest(params.slug)
    }
}