const loginForm = document.getElementById('login-form')
const baseEndpoint = "http://localhost:8000/api"
const coontainer = document.getElementById('container')

if (loginForm){
    loginForm.addEventListener('submit', handleLogin)
}

function writeContainer(data) {
    if (container){
        container.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "</pre>"
    }
}

function handleLogin(event){
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    let bodyString = JSON.stringify(loginObjectData)
    console.log(loginObjectData, bodyString)
    const options = {
        method:"POST",
        headers: {
            "content-type":"application/json"
        },
        body: bodyString
    }
    fetch(loginEndpoint, options)
    .then(response=>{
        console.log(response)
        return response.json()
    })
    .then(authData => {
        handleAuthData(authData, getProductList)
    })
    .catch(err=>{
        console.log(err)
    })
}

function handleAuthData(authData, callback) {
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)
    if (callback){
        callback()
    }
}

function tokenNotValid(jsonData) {
    if (jsonData.code && jsonData.code === "token_not_valid"){
        //run a refresh token query
        alert("please login again")
        return false
    }
    return true
}

function getProductList() {
    const endpoint = `${baseEndpoint}/products`
    const options = {
        method:"GET",
        headers: {
            "content-type":"application/json",
            'Authorization': `Bearer ${localStorage.getItem('access')}`
        }
    }
    fetch(endpoint, options)
    .then(response=>{
        return response.json()
    })
    .then(data=>{
        console.log(data)
        if (tokenNotValid(data)){
            writeContainer(data)
        }
    })
}