const express = require('express');
const bodyParser = require('body-parser');
const { Pool } = require('pg');

// Configuración de PostgreSQL
const pool = new Pool({
    user: 'tu_usuario',
    host: 'localhost',
    database: 'tu_base_de_datos',
    password: 'tu_contraseña',
    port: 5432,
});

const app = express();
app.use(bodyParser.json());
app.use(express.static('public')); // Servir archivos estáticos como el HTML y CSS

// Ruta de búsqueda
app.post('/search', async (req, res) => {
    const { nombre, idNombre, departamento, idDepartamento } = req.body;
    try {
        const result = await pool.query(
            `SELECT * FROM equipos 
             WHERE 
                ($1::text IS NULL OR nombre_generico ILIKE '%' || $1 || '%') AND
                ($2::text IS NULL OR id::text = $2) AND
                ($3::text IS NULL OR departamento ILIKE '%' || $3 || '%') AND
                ($4::text IS NULL OR id_departamento::text = $4)`,
            [nombre, idNombre, departamento, idDepartamento]
        );
        res.json(result.rows);
    } catch (error) {
        console.error('Error querying database:', error);
        res.status(500).send('Error en el servidor');
    }
});

// Iniciar servidor
app.listen(3000, () => {
    console.log('Servidor escuchando en http://localhost:3000');
});
