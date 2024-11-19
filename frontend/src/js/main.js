document.getElementById("loginForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente
    
    // Puedes agregar lógica para validar las credenciales aquí, si es necesario.
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Simulamos una validación básica para redirigir según el resultado
    if (username === "adminimss" && password === "admin00") {
        window.location.href = "./views/dashboard.html"; 
    } else {
        alert("Credenciales incorrectas. Por favor, intente de nuevo.");
    }
});