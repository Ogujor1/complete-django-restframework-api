const loginForm = document.getElementById('login-form')
const baseEndpoint = "http://localhost:8000/api"
if (loginForm) {
  loginForm = addEventListener('submit', handleLogin)
}

function handleLogin (event) {
  console.log(event)
  event.preventDefault()
  const loginEndpoint = `${baseEndpoint}/token/`
  let loginFormData = new FormData(loginForm)
  let loginObjectData = Object.fromEntries(loginFormData)
  console.log(loginObjectData['username'])
  let bodystr = JSON.stringify(loginObjectData)
  const options = {
    method : "POST",
    header: {
      "ContentType": "application/json"
    },
    body: bodystr
  }
  fetch(loginEndpoint, options)
}