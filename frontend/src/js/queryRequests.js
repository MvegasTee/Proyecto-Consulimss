document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('search-form');
    const resultList = document.getElementById('result-list');
    const detalleEquipo = document.getElementById('detalle-equipo');
    const imagenEquipo = document.getElementById('imagen-equipo');
    const statusEquipo = document.getElementById('status');
    const accesoriosEquipo = document.getElementById('accesorios');
    const descripcionEquipo = document.getElementById('descripcion');

    // Enviar consulta al servidor al enviar el formulario
    searchForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const query = {
            nombre: document.getElementById('nombre').value,
            idNombre: document.getElementById('id-nombre').value,
            departamento: document.getElementById('departamento').value,
            idDepartamento: document.getElementById('id-departamento').value,
        };

        try {
            const response = await fetch('/search', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(query),
            });

            const results = await response.json();
            renderResults(results);
        } catch (error) {
            console.error('Error fetching search results:', error);
        }
    });

    // Mostrar resultados en la lista
    function renderResults(results) {
        resultList.innerHTML = ''; // Limpiar resultados anteriores
        results.forEach((item) => {
            const listItem = document.createElement('li');
            listItem.textContent = item.nombre_generico;
            listItem.addEventListener('click', () => loadDetails(item));
            resultList.appendChild(listItem);
        });
    }

    // Cargar detalles del equipo al hacer clic en un resultado
    function loadDetails(item) {
        imagenEquipo.src = item.imagen || '';
        imagenEquipo.style.display = item.imagen ? 'block' : 'none';
        statusEquipo.value = item.status || 'Sin información';
        accesoriosEquipo.textContent = item.accesorios || 'No disponible';
        descripcionEquipo.value = item.descripcion || 'Sin descripción';
    }
});
