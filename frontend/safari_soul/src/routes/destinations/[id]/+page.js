export async function load({fetch, params}){
    
    const fetchDest = async (id) => {
        const endpoint = `http://0.0.0.0:8000/api/destinations/${id}`
        const result = await fetch(endpoint)
        const data = await result.json()
        return data
    }
    return {
       destination: fetchDest(params.id)
    }
}