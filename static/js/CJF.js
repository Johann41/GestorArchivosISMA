const lista_organos_jurisdiccionales = async (Id)=>{
    try {
        const response = await fetch(`./organo_jurisdiccional/${Id}`)
        const data = await response.json()
        // console.log(data)        
        if(data.msg==="Success"){
            let opciones=''
            data.organos_j.forEach(organo_j => {
                opciones+=`<option value='${organo_j.id}'>${organo_j.nombre}</option>`          
            });
            organo.innerHTML=opciones       
        }else{
            alert('organos no encontrados')
        }

    } catch (error) {
        console.log(error)
    }
}

const listar_circuitos = async () =>{
    try {      
        const response = await fetch("./circuitos")
        const data = await response.json()

        if(data.msg === "Success"){
            let opciones = ''
            data.circuitos.forEach( circuirto => {
                opciones+=`<option value='${circuirto.id}'>${circuirto.nombre}</option>`
            })
            circuito.innerHTML=opciones
            lista_organos_jurisdiccionales(data.circuitos[0].id)
        }else{
            alert('circuitos no encontrados')
        }

    } catch (error) {
        console.log(error)
    }
}

const cargaInicial = async()=>{
    await listar_circuitos()
    distrito.addEventListener("change", (event) =>{     
        lista_organos_jurisdiccionales(event.target.value)
    })
    
}

window.addEventListener("load", async()=>{
    cargaInicial()
})

if (window.history.replaceState) { // verificamos disponibilidad
    window.history.replaceState(null, null, window.location.href);
}